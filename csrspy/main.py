"""Module for transforming coordinates between different reference frames.

Transforms coordinates between different reference frames, epochs, and vertical datums.

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyproj import CRS, Transformer

if TYPE_CHECKING:
    from collections.abc import Iterable
from pyproj.enums import TransformDirection

from csrspy.enums import CoordType, Reference, VerticalDatum
from csrspy.factories import HelmertFactory, VerticalGridShiftFactory

EPS = 1e-8

T_Coord3D = tuple[float, float, float]
T_Coord4D = tuple[float, float, float, float]


class _ToNAD83:
    direction = TransformDirection.FORWARD

    def __init__(
        self,
        s_ref_frame: Reference | str,
        s_coords: str | CoordType,
        s_epoch: float,
        s_vd: VerticalDatum | str = VerticalDatum.GRS80,
        t_coords: str | CoordType | None = None,
        t_epoch: float | None = None,
        t_vd: VerticalDatum | str = VerticalDatum.GRS80,
        epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif",
    ) -> None:
        super().__init__()
        self.s_ref_frame = (
            Reference.ITRF14 if s_ref_frame == Reference.WGS84 else s_ref_frame
        )
        self.s_coords = s_coords
        self.t_coords = t_coords if t_coords is not None else s_coords
        self.s_epoch = s_epoch
        self.t_epoch = t_epoch if t_epoch is not None else s_epoch
        self.s_vd = s_vd
        self.t_vd = t_vd
        self.epoch_shift_grid = epoch_shift_grid

        self.transforms = []

        # 1. ITRFxx GRS80 / WGS84  -> ECEF GRS80
        in_crs = CRS.from_proj4(
            self._coord_type_to_proj4(
                self.s_coords,
                VerticalDatum.WGS84
                if self.s_vd == VerticalDatum.WGS84
                else VerticalDatum.GRS80,
            )
        )
        grs80_crs = CRS.from_proj4("+proj=cart +ellps=GRS80")
        transform_in2cartestian = Transformer.from_crs(in_crs, grs80_crs)
        self.transforms.append(transform_in2cartestian)

        # 2. ECEF GRS80 -> NAD83
        transform_helmert = HelmertFactory.from_ref_frame(self.s_ref_frame).transformer
        self.transforms.append(transform_helmert)

        # 3. NAD83(CSRS) Ellips s_epoch -> NAD83(CSRS) Ellips t_epoch
        if abs(self.t_epoch - self.s_epoch) > EPS:
            # Epoch shift transform
            epoch_shift_proj_str = (
                f"+inv +proj=deformation "
                f"+t_epoch={self.t_epoch:.5f} +grids={self.epoch_shift_grid}"
            )
            transform_epoch_shift = Transformer.from_pipeline(epoch_shift_proj_str)
            self.transforms.append(transform_epoch_shift)

        # 4. Convert cartographic coords to lonlat in radians
        transform_lonlat2rad = Transformer.from_pipeline("+inv +proj=cart +ellps=GRS80")
        self.transforms.append(transform_lonlat2rad)

        # 5. NAD83(CSRS) Ellips t_epoch -> NAD83(CSRS) Orthometric t_epoch
        transform_vshift = VerticalGridShiftFactory(self.t_vd).transformer
        self.transforms.append(transform_vshift)

        # 6. Final transform to output
        transform_out = Transformer.from_pipeline(
            self._coord_type_to_proj4(self.t_coords)
        )
        self.transforms.append(transform_out)

    @staticmethod
    def _coord_type_to_proj4(
        coord_type: CoordType | str,
        ellps: VerticalDatum | str = VerticalDatum.GRS80,
    ) -> str:
        ellps = ellps.upper()

        if coord_type == CoordType.GEOG:
            return f"+proj=longlat +ellps={ellps} +no_defs"
        if coord_type == CoordType.CART:
            return f"+proj=cart +ellps={ellps} +no_defs"
        zone = int(coord_type.value[3:])
        return f"+proj=utm +zone={zone} +ellps={ellps} +units=m +no_defs"

    def _coord_3d_to_4d(self, coord: T_Coord3D) -> T_Coord4D:
        return coord[0], coord[1], coord[2], self.s_epoch

    @staticmethod
    def _coord_4d_to_3d(coord: T_Coord4D) -> T_Coord3D:
        return coord[0], coord[1], coord[2]

    def __call__(self, coords: Iterable[T_Coord3D]) -> Iterable[T_Coord3D]:
        """Transform coordinates from s_ref_frame, s_crs, s_epoch to Nad83(CSRS).

        `t_epoch`, `t_vd`, with coordinate type `out`.

        Args:
            coords: An iterable of 3D coordinates in the s_ref_frame, s_crs, s_epoch.

        Return:
            An iterable of 3D coordinates in the Nad83(CSRS), `t_epoch`, `t_vd`, `out`.

        """
        coords = map(self._coord_3d_to_4d, coords)
        for trans in self.transforms:
            coords = trans.itransform(coords, direction=self.direction)
        return map(self._coord_4d_to_3d, coords)


class _FromNAD83(_ToNAD83):
    """The same as _toNAD83, but does all transformations in reverse."""

    direction = TransformDirection.INVERSE

    def __init__(
        self,
        t_ref_frame: Reference | str,
        t_coords: str | CoordType,
        t_epoch: float,
        t_vd: VerticalDatum | str = VerticalDatum.GRS80,
        s_coords: str | CoordType | None = None,
        s_epoch: float | None = None,
        s_vd: VerticalDatum | str = VerticalDatum.GRS80,
        epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif",
    ) -> None:
        super().__init__(
            s_ref_frame=t_ref_frame,
            s_coords=t_coords,
            s_epoch=t_epoch,
            s_vd=t_vd,
            t_coords=s_coords,
            t_epoch=s_epoch,
            t_vd=s_vd,
            epoch_shift_grid=epoch_shift_grid,
        )
        self.transforms.reverse()


class CSRSTransformer:
    """The main coordinate transformation object.

    Args:
        s_ref_frame: The source reference frame.
            e.g. "itrf14", "nad83csrs" or one of type `csrspy.enums.Ref` enumerated
            values.
        s_coords: The source coordinate type.
            e.g. "geog", "cart", "utm10", "utm22"
        s_epoch: The source epoch in decimal year format.
            e.g. `2010.5` to specify julian day 0.5 * 365 (June?) of the year 2010.
        s_vd: The source orthometric heights model.
            See `csrspy.enums.Geoid` for options.
        t_ref_frame: The target reference frame.
            e.g. "itrf14", "nad83csrs" or one of type `csrspy.enums.Ref` enumerated
            values.
        t_coords: The target coordinate type.
            e.g. "geog", "cart", "utm10", "utm22"
        t_epoch: The target epoch in decimal year format.
            e.g. `2010.5` to specify day 365/2 (June?) of the year 2010.
        t_vd: The target orthometric heights model.
            See `csrspy.enums.Geoid` for options.
        epoch_shift_grid: The name of the proj grid file used for epoch transformations.
            Defaults to "ca_nrc_NAD83v70VG.tif"

    Raises:
        ValueError: If VerticalDatum and RefFrame are incompatible with each other.

    """

    def __init__(
        self,
        *,
        s_ref_frame: Reference | str,
        s_coords: str | CoordType,
        s_epoch: float,
        s_vd: VerticalDatum | str | None = None,
        t_ref_frame: Reference | str,
        t_coords: str | CoordType | None = None,
        t_epoch: float | None = None,
        t_vd: VerticalDatum | str | None = None,
        epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif",
    ) -> None:
        """Initialize the CSRSTransformer.

        Args:
            s_ref_frame: The source reference frame.
            s_coords: The source coordinate type.
            s_epoch: The source epoch in decimal year format.
            s_vd: The source orthometric heights model.
            t_ref_frame: The target reference frame.
            t_coords: The target coordinate type.
            t_epoch: The target epoch in decimal year format.
            t_vd: The target orthometric heights model.
            epoch_shift_grid: The name of the proj grid file used for epoch
                transformations.

        Raises:
            ValueError: If the reference frame and vertical datum are incompatible.

        """
        super().__init__()
        self.s_ref_frame = s_ref_frame
        self.t_ref_frame = t_ref_frame
        self.s_coords = s_coords
        self.t_coords = t_coords if t_coords is not None else s_coords
        self.s_epoch = s_epoch
        self.t_epoch = t_epoch if t_epoch is not None else s_epoch
        self.s_vd = s_vd
        self.t_vd = t_vd if t_vd is not None else s_vd
        self.epoch_shift_grid = epoch_shift_grid

        self.validate_crs(s_ref_frame, s_vd)
        self.validate_crs(t_ref_frame, t_vd)

        if (not self.is_nad83(s_ref_frame)) and self.is_nad83(t_ref_frame):
            self.transformers = [
                _ToNAD83(
                    s_ref_frame=self.s_ref_frame,
                    s_coords=self.s_coords,
                    s_epoch=self.s_epoch,
                    s_vd=self.s_vd,
                    t_coords=self.t_coords,
                    t_epoch=self.t_epoch,
                    t_vd=self.t_vd,
                    epoch_shift_grid=self.epoch_shift_grid,
                )
            ]

        elif self.is_nad83(s_ref_frame) and (not self.is_nad83(t_ref_frame)):
            self.transformers = [
                _FromNAD83(
                    t_ref_frame=self.t_ref_frame,
                    t_coords=self.t_coords,
                    t_epoch=self.t_epoch,
                    t_vd=self.t_vd,
                    s_coords=self.s_coords,
                    s_epoch=self.s_epoch,
                    s_vd=self.s_vd,
                    epoch_shift_grid=self.epoch_shift_grid,
                )
            ]

        elif not (self.is_nad83(s_ref_frame) or self.is_nad83(t_ref_frame)):
            self.transformers = [
                _ToNAD83(
                    s_ref_frame=self.s_ref_frame,
                    s_coords=self.s_coords,
                    s_epoch=self.s_epoch,
                    s_vd=self.s_vd,
                    t_coords=self.t_coords,
                    t_epoch=self.t_epoch,
                    t_vd=VerticalDatum.GRS80,
                    epoch_shift_grid=self.epoch_shift_grid,
                ),
                _FromNAD83(
                    t_ref_frame=self.t_ref_frame,
                    t_coords=self.t_coords,
                    t_epoch=self.t_epoch,
                    t_vd=self.t_vd,
                    s_coords=self.t_coords,
                    s_epoch=self.t_epoch,
                    s_vd=VerticalDatum.GRS80,
                    epoch_shift_grid=self.epoch_shift_grid,
                ),
            ]

        elif self.is_nad83(s_ref_frame) and self.is_nad83(t_ref_frame):
            self.transformers = [
                _FromNAD83(
                    t_ref_frame=Reference.ITRF14,
                    t_coords=self.t_coords,
                    t_epoch=self.t_epoch,
                    t_vd=self.t_vd,
                    s_coords=self.s_coords,
                    s_epoch=self.s_epoch,
                    s_vd=self.s_vd,
                    epoch_shift_grid=self.epoch_shift_grid,
                ),
                _ToNAD83(
                    s_ref_frame=Reference.ITRF14,
                    s_coords=self.t_coords,
                    s_epoch=self.t_epoch,
                    s_vd=self.t_vd,
                    t_coords=self.t_coords,
                    t_epoch=self.t_epoch,
                    t_vd=self.t_vd,
                    epoch_shift_grid=self.epoch_shift_grid,
                ),
            ]

    @staticmethod
    def is_nad83(ref_frame: Reference) -> bool:
        """Check if the reference frame is NAD83(CSRS).

        Args:
            ref_frame: The reference frame to check.

        Returns:
            bool: True if the reference frame is NAD83(CSRS), False otherwise.

        """
        return ref_frame == Reference.NAD83CSRS

    @staticmethod
    def is_itrf(ref_frame: Reference) -> bool:
        """Check if the reference frame is ITRF.

        Args:
            ref_frame: The reference frame to check.

        Returns:
            bool: True if the reference frame is ITRF, False otherwise.

        """
        return ref_frame not in {Reference.NAD83CSRS, Reference.WGS84}

    @staticmethod
    def is_wgs84(ref_frame: Reference) -> bool:
        """Check if the reference frame is WGS84.

        Args:
            ref_frame: The reference frame to check.

        Returns:
            bool: True if the reference frame is WGS84, False otherwise.

        """
        return ref_frame == Reference.WGS84

    def validate_crs(self, ref_frame: Reference, vd: VerticalDatum | None) -> None:
        """Validate the reference frame and vertical datum compatibility.

        Args:
            ref_frame: The reference frame to validate.
            vd: The vertical datum to validate.

        Raises:
            ValueError: If the reference frame and vertical datum are incompatible.

        """
        if self.is_itrf(ref_frame) and vd is not VerticalDatum.GRS80:
            msg = f"{ref_frame} must use VerticalDatum GRS80."
            raise ValueError(msg)
        if self.is_wgs84(ref_frame) and vd not in [
            VerticalDatum.WGS84,
            VerticalDatum.GRS80,
        ]:
            msg = f"{ref_frame} must use VerticalDatum WGS84 or GRS80."
            raise ValueError(msg)
        if self.is_nad83(ref_frame) and vd is VerticalDatum.WGS84:
            msg = f"{ref_frame} must not use VerticalDatum WGS84."
            raise ValueError(msg)

    def __call__(self, coords: Iterable[T_Coord3D]) -> Iterable[T_Coord3D]:
        """Transform coordinates from s_ref_frame, s_crs, s_epoch to Nad83(CSRS).

        `t_epoch`, `t_vd`, with coordinate type `out`.

        Args:
            coords: A list of 3D coordinates to transform
        Returns:
            A list of transformed 3D coordinates

        """
        for transformer in self.transformers:
            coords = transformer(coords)

        return coords
