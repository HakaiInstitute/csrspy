from typing import Iterable, Optional, Union

from pyproj import CRS, Transformer

from csrspy.datatypes import Coordinate, Geoid, Ref
from csrspy.factories import HelmertFactory, VerticalGridShiftFactory


class CSRSTransformer(object):
    def __init__(self, s_ref_frame: Ref, s_crs: Union[str, int], s_epoch: float, t_epoch: Optional[float] = None,
                 t_vd: Optional[Geoid] = None, out: str = "geog", epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif"):
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

    def forward(self, coords: Iterable[Coordinate]) -> Iterable[Coordinate]:
        coords = list(coord.to_tuple(self.s_epoch) for coord in coords)
        for p in self.transforms:
            coords = list(p.itransform(coords))
        return list(Coordinate.from_tuple((coord[0], coord[1], coord[2], self.t_epoch)) for coord in coords)

    def backward(self):
        return NotImplementedError
