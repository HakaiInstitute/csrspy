from typing import Iterable, Optional, Tuple, Union

from pyproj import CRS, Transformer
from pyproj.enums import TransformDirection

from csrspy.enums import CoordType, VerticalDatum, Reference
from csrspy.factories import HelmertFactory, VerticalGridShiftFactory

T_Coord3D = Tuple[float, float, float]
T_Coord4D = Tuple[float, float, float, float]


class _ToNAD83:
    direction = TransformDirection.FORWARD

    def __init__(self, s_ref_frame: Union[Reference, str], s_coords: Union[str, CoordType],
                 s_epoch: float, s_vd: Union[VerticalDatum, str] = VerticalDatum.GRS80,
                 t_coords: Union[str, CoordType] = None, t_epoch: float = None,
                 t_vd: Union[VerticalDatum, str] = VerticalDatum.GRS80,
                 epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif"):
        super().__init__()
        self.s_ref_frame = Reference.ITRF14 if s_ref_frame == Reference.WGS84 else s_ref_frame
        self.s_coords = s_coords
        self.t_coords = t_coords if t_coords is not None else s_coords
        self.s_epoch = s_epoch
        self.t_epoch = t_epoch if t_epoch is not None else s_epoch
        self.s_vd = s_vd
        self.t_vd = t_vd
        self.epoch_shift_grid = epoch_shift_grid

        self.transforms = []

        # 1. ITRFxx GRS80 / WGS84  -> ECEF GRS80
        in_crs = CRS.from_proj4(self._coord_type_to_proj4(
            self.s_coords,
            VerticalDatum.WGS84 if self.s_vd == VerticalDatum.WGS84 else VerticalDatum.GRS80)
        )
        grs80_crs = CRS.from_proj4("+proj=cart +ellps=GRS80")
        transform_in2cartestian = Transformer.from_crs(in_crs, grs80_crs)
        self.transforms.append(transform_in2cartestian)

        # 2. ECEF GRS80 -> NAD83
        transform_helmert = HelmertFactory.from_ref_frame(self.s_ref_frame).transformer
        self.transforms.append(transform_helmert)

        # 3. NAD83(CSRS) Ellips s_epoch -> NAD83(CSRS) Ellips t_epoch
        if abs(self.t_epoch - self.s_epoch) > 1e-8:
            # Epoch shift transform
            epoch_shift_proj_str = f"+inv +proj=deformation +t_epoch={self.t_epoch:.5f} +grids={self.epoch_shift_grid}"
            transform_epoch_shift = Transformer.from_pipeline(epoch_shift_proj_str)
            self.transforms.append(transform_epoch_shift)

        # 4. Convert cartographic coords to lonlat in radians
        transform_lonlat2rad = Transformer.from_pipeline("+inv +proj=cart +ellps=GRS80")
        self.transforms.append(transform_lonlat2rad)

        # 5. NAD83(CSRS) Ellips t_epoch -> NAD83(CSRS) Orthometric t_epoch
        transform_vshift = VerticalGridShiftFactory(self.t_vd).transformer
        self.transforms.append(transform_vshift)

        # 6. Final transform to output
        transform_out = Transformer.from_pipeline(self._coord_type_to_proj4(self.t_coords))
        self.transforms.append(transform_out)

    @staticmethod
    def _coord_type_to_proj4(coord_type: Union[CoordType, str],
                             ellps: Union[VerticalDatum, str] = VerticalDatum.GRS80) -> str:
        ellps = ellps.upper()

        if coord_type == CoordType.GEOG:
            return f"+proj=longlat +ellps={ellps} +no_defs"
        if coord_type == CoordType.CART:
            return f"+proj=cart +ellps={ellps} +no_defs"
        else:
            zone = int(coord_type.value[3:])
            return f"+proj=utm +zone={zone} +ellps={ellps} +units=m +no_defs"

    def _coord_3d_to_4d(self, coord: T_Coord3D) -> T_Coord4D:
        return coord[0], coord[1], coord[2], self.s_epoch

    @staticmethod
    def _coord_4d_to_3d(coord: T_Coord4D) -> T_Coord3D:
        return coord[0], coord[1], coord[2]

    def __call__(self, coords: Iterable[T_Coord3D]) -> Iterable[T_Coord3D]:
        """
        Transform the coordinates from the s_ref_frame, s_crs, s_epoch to Nad83(CSRS), `t_epoch`, `t_vd`, with coordinate type `out`.
        :param coords:
        :return:
        """
        coords = map(self._coord_3d_to_4d, coords)
        for trans in self.transforms:
            coords = trans.itransform(coords, direction=self.direction)
        return map(self._coord_4d_to_3d, coords)


class _FromNAD83(_ToNAD83):
    """This class is the same as toNAD83, but does all transformations in reverse."""
    direction = TransformDirection.INVERSE

    def __init__(self, t_ref_frame: Union[Reference, str], t_coords: Union[str, CoordType],
                 t_epoch: float, t_vd: Union[VerticalDatum, str] = VerticalDatum.GRS80,
                 s_coords: Union[str, CoordType] = None, s_epoch: float = None,
                 s_vd: Union[VerticalDatum, str] = VerticalDatum.GRS80,
                 epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif"):
        super().__init__(s_ref_frame=t_ref_frame, s_coords=t_coords, s_epoch=t_epoch,
                         s_vd=t_vd, t_coords=s_coords, t_epoch=s_epoch, t_vd=s_vd,
                         epoch_shift_grid=epoch_shift_grid)
        self.transforms.reverse()


class CSRSTransformer(object):
    def __init__(self, *, s_ref_frame: Union[Reference, str], s_coords: Union[str, CoordType],
                 s_epoch: float, s_vd: Union[VerticalDatum, str] = None,
                 t_ref_frame: Union[Reference, str], t_coords: Union[str, CoordType] = None,
                 t_epoch: float = None, t_vd: Union[VerticalDatum, str] = None,
                 epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif"):
        """
        Creates a coordinate transformation object with configured source and target reference systems.

        :param s_ref_frame: The source reference frame. eg. "itrf14", "nad83csrs" or one of type `csrspy.enums.Ref` enumerated values.
        :param s_coords: The source coordinate type. eg. "geog", "cart", "utm10", "utm22"
        :param s_epoch: The source epoch in decimal year format. eg. `2010.5` to specify day 365/2 (June?) of the year 2010.
        :param s_vd: The source orthometric heights model. See `csrspy.enums.Geoid` for options.
        :param t_ref_frame: The target reference frame. eg. "itrf14", "nad83csrs" or one of type `csrspy.enums.Ref` enumerated values.
        :param t_coords: The target coordinate type. eg. "geog", "cart", "utm10", "utm22"
        :param t_epoch: The target epoch in decimal year format. eg. `2010.5` to specify day 365/2 (June?) of the year 2010.
        :param t_vd: The target orthometric heights model. See `csrspy.enums.Geoid` for options.
        :param epoch_shift_grid: The name of the proj grid file used for epoch transformations. Defaults to "ca_nrc_NAD83v70VG.tif"
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
            self.transformers = [_ToNAD83(s_ref_frame=self.s_ref_frame, s_coords=self.s_coords,
                                          s_epoch=self.s_epoch, s_vd=self.s_vd,
                                          t_coords=self.t_coords, t_epoch=self.t_epoch,
                                          t_vd=self.t_vd,
                                          epoch_shift_grid=self.epoch_shift_grid)]

        elif self.is_nad83(s_ref_frame) and (not self.is_nad83(t_ref_frame)):
            self.transformers = [_FromNAD83(t_ref_frame=self.t_ref_frame, t_coords=self.t_coords,
                                            t_epoch=self.t_epoch, t_vd=self.t_vd,
                                            s_coords=self.s_coords, s_epoch=self.s_epoch,
                                            s_vd=self.s_vd,
                                            epoch_shift_grid=self.epoch_shift_grid)]

        elif not (self.is_nad83(s_ref_frame) or self.is_nad83(t_ref_frame)):
            self.transformers = [
                _ToNAD83(s_ref_frame=self.s_ref_frame, s_coords=self.s_coords,
                         s_epoch=self.s_epoch, s_vd=self.s_vd,
                         t_coords=self.t_coords, t_epoch=self.t_epoch, t_vd=VerticalDatum.GRS80,
                         epoch_shift_grid=self.epoch_shift_grid),
                _FromNAD83(t_ref_frame=self.t_ref_frame, t_coords=self.t_coords,
                           t_epoch=self.t_epoch, t_vd=self.t_vd,
                           s_coords=self.t_coords, s_epoch=self.t_epoch, s_vd=VerticalDatum.GRS80,
                           epoch_shift_grid=self.epoch_shift_grid)
            ]

        elif self.is_nad83(s_ref_frame) and self.is_nad83(t_ref_frame):
            self.transformers = [
                _FromNAD83(t_ref_frame=Reference.ITRF14, t_coords=self.t_coords,
                           t_epoch=self.t_epoch, t_vd=self.t_vd,
                           s_coords=self.s_coords, s_epoch=self.s_epoch, s_vd=self.s_vd,
                           epoch_shift_grid=self.epoch_shift_grid),
                _ToNAD83(s_ref_frame=Reference.ITRF14, s_coords=self.t_coords,
                         s_epoch=self.t_epoch, s_vd=self.t_vd,
                         t_coords=self.t_coords, t_epoch=self.t_epoch, t_vd=self.t_vd,
                         epoch_shift_grid=self.epoch_shift_grid),
            ]

    @staticmethod
    def is_nad83(ref_frame: Reference):
        return ref_frame == Reference.NAD83CSRS

    @staticmethod
    def is_itrf(ref_frame: Reference):
        return ref_frame != Reference.NAD83CSRS and ref_frame != Reference.WGS84

    @staticmethod
    def is_wgs84(ref_frame: Reference):
        return ref_frame == Reference.WGS84

    def validate_crs(self, ref_frame: Reference, vd: Optional[VerticalDatum]):
        if self.is_itrf(ref_frame):
            assert vd is VerticalDatum.GRS80, \
                f"{ref_frame} must use VerticalDatum GRS80."
        elif self.is_wgs84(ref_frame):
            assert (vd is VerticalDatum.WGS84) or (vd is VerticalDatum.GRS80), \
                f"{ref_frame} must use VerticalDatum WGS84 or GRS80."
        elif self.is_nad83(ref_frame):
            assert vd is not VerticalDatum.WGS84, \
                f"{ref_frame} must not use VerticalDatum WGS84."

    def __call__(self, coords: Iterable[T_Coord3D]) -> Iterable[T_Coord3D]:
        """
        Transform the coordinates from the s_ref_frame, s_crs, s_epoch to Nad83(CSRS), `t_epoch`, `t_vd`, with coordinate type `out`.
        :param coords:
        :return:
        """

        for transformer in self.transformers:
            coords = transformer(coords)

        return coords
