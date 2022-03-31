from typing import Iterable, Optional, Tuple, Union

from pyproj import CRS, Transformer
from pyproj.enums import TransformDirection

from csrspy.enums import Geoid, Ref
from csrspy.factories import HelmertFactory, VerticalGridShiftFactory

T_Coord3D = Tuple[float, float, float]
T_Coord4D = Tuple[float, float, float, float]


class CSRSTransformer(object):
    def __init__(self, s_ref_frame: Union[Ref, str], s_crs: Union[str, int], s_epoch: float, t_epoch: Optional[float] = None,
                 t_vd: Optional[Union[Geoid, str]] = None, out: str = "geog", epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif"):
        """
        Creates a coordinate transformation object with configured source and target reference systems.

        :param s_ref_frame:
        :param s_crs:
        :param s_epoch:
        :param t_epoch:
        :param t_vd:
        :param out:
        """
        super().__init__()
        self.s_epoch = s_epoch
        self.t_epoch = t_epoch if t_epoch is not None else s_epoch
        self.transforms = []

        # 1. ITRFxx Ellips -> NAD83(CSRS) Ellips
        in_crs = CRS.from_user_input(s_crs)
        grs80_crs = CRS.from_proj4("+proj=cart +ellps=GRS80")
        transform_in2cartestian = Transformer.from_crs(in_crs, grs80_crs)
        self.transforms.append(transform_in2cartestian)

        transform_helmert = HelmertFactory.from_ref_frame(s_ref_frame).transformer
        self.transforms.append(transform_helmert)

        # 2. NAD83(CSRS) Ellips s_epoch -> NAD83(CSRS) Ellips t_epoch
        if t_epoch is not None and abs(t_epoch - s_epoch) > 1e-8:
            # Epoch shift transform
            epoch_shift_proj_str = f"+inv +proj=deformation +t_epoch={t_epoch:.5f} +grids={epoch_shift_grid}"
            transform_epoch_shift = Transformer.from_pipeline(epoch_shift_proj_str)
            self.transforms.append(transform_epoch_shift)

        # Convert cartographic coords to lonlat in radians
        transform_lonlat2rad = Transformer.from_pipeline("+inv +proj=cart +ellps=GRS80")
        self.transforms.append(transform_lonlat2rad)

        # 3. NAD83(CSRS) Ellips t_epoch -> NAD83(CSRS) Orthometric t_epoch
        transform_vshift = VerticalGridShiftFactory(t_vd).transformer
        self.transforms.append(transform_vshift)

        # 4. Final transform to output
        if out == "cart":
            transform_out = Transformer.from_pipeline("+proj=cart")

        elif out[:3] == "utm":
            zone = int(out[3:])
            transform_out = Transformer.from_pipeline(f"+proj=utm +zone={zone}")

        else:  # out == "geog":
            # Convert lonlat in radians to latlon in degrees
            transform_out = Transformer.from_pipeline(
                "+proj=pipeline +step +proj=unitconvert +xy_in=rad +xy_out=deg +step +proj=axisswap +order=2,1")

        self.transforms.append(transform_out)

    def _coord_3d_to_4d(self, coord: T_Coord3D) -> T_Coord4D:
        return coord[0], coord[1], coord[2], self.s_epoch

    @staticmethod
    def _coord_4d_to_3d(coord: T_Coord4D) -> T_Coord3D:
        return coord[0], coord[1], coord[2]

    def forward(self, coords: Iterable[T_Coord3D]) -> Iterable[T_Coord3D]:
        coords = map(self._coord_3d_to_4d, coords)
        for p in self.transforms:
            coords = p.itransform(coords)
        return map(self._coord_4d_to_3d, coords)

    def backward(self, coords: Iterable[T_Coord3D]) -> Iterable[T_Coord3D]:
        coords = map(self._coord_3d_to_4d, coords)
        for p in self.transforms[::-1]:
            coords = p.itransform(coords, direction=TransformDirection.INVERSE)
        return map(self._coord_4d_to_3d, coords)
