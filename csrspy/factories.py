from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from pyproj import Transformer

from csrspy.enums import VerticalDatum, Reference


class Factory(ABC):
    @property
    @abstractmethod
    def proj_str(self) -> str:
        raise NotImplementedError

    @property
    def transformer(self):
        return Transformer.from_pipeline(self.proj_str)


@dataclass(frozen=True)
class HelmertFactory(Factory):
    x: float
    dx: float
    y: float
    dy: float
    z: float
    dz: float
    rx: float
    drx: float
    ry: float
    dry: float
    rz: float
    drz: float
    s: float
    ds: float
    itrf_epoch: float = 2010

    @property
    def proj_str(self):
        return f"proj=helmert convention=position_vector t_epoch={self.itrf_epoch:.3f} " \
               f"x={self.x:.8f} dx={self.dx:.8f} " \
               f"y={self.y:.8f} dy={self.dy:.8f} " \
               f"z={self.z:.8f} dz={self.dz:.8f} " \
               f"rx={self.rx * 1e-3:.8f} drx={self.drx * 1e-3:.8f} " \
               f"ry={self.ry * 1e-3:.8f} dry={self.dry * 1e-3:.8f} " \
               f"rz={self.rz * 1e-3:.8f} drz={self.drz * 1e-3:.8f} " \
               f"s={self.s * 1e-3:.8f} ds={self.ds * 1e-3:.8f}"

    @classmethod
    def from_ref_frame(cls, ref_frame: Reference):
        if ref_frame == Reference.NAD83CSRS:
            return cls(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2010)

        elif ref_frame == Reference.ITRF88:
            return cls(0.97300, 0.00000, -1.90720, 0.00000, -0.42090, 0.00000, -26.58160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, -7.40000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF89:
            return cls(0.96800, 0.00000, -1.94320, 0.00000, -0.44490, 0.00000, -26.48160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, -4.30000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF90:
            return cls(0.97300, 0.00000, -1.91920, 0.00000, -0.48290, 0.00000, -26.48160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, -0.90000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF91:
            return cls(0.97100, 0.00000, -1.92320, 0.00000, -0.49890, 0.00000, -26.48160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, -0.60000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF92:
            return cls(0.98300, 0.00000, -1.90920, 0.00000, -0.50490, 0.00000, -26.48160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, 0.80000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF93:
            return cls(1.04880, 0.00290, -1.91100, -0.00040, -0.51550, -0.00080, -23.67160, 0.05680, 3.37990, 0.93230,
                       -11.38920, -0.01840, -0.40000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF94:
            return cls(0.99100, 0.00000, -1.90720, 0.00000, -0.51290, 0.00000, -26.48160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, 0.00000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF96:
            return cls(0.99100, 0.00000, -1.90720, 0.00000, -0.51290, 0.00000, -26.48160, -0.05320, -0.00010, 0.74230,
                       -11.24920, 0.03160, 0.00000, 0.00000, 2010)

        elif ref_frame == Reference.ITRF97:
            return cls(0.99790, 0.00069, -1.90871, -0.00010, -0.47877, 0.00186, -26.78138, -0.06667, 0.42027, 0.75744,
                       -11.19206, 0.03133, -3.43109, -0.19201, 2010)

        elif ref_frame == Reference.ITRF00:
            return cls(1.00460, 0.00069, -1.91041, -0.00070, -0.51547, 0.00046, -26.78138, -0.06667, 0.42027, 0.75744,
                       -10.93206, 0.05133, -1.75109, -0.18201, 2010)

        elif ref_frame == Reference.ITRF05:
            return cls(1.00270, 0.00049, -1.91021, -0.00060, -0.53927, -0.00134, -26.78138, -0.06667, 0.42027, 0.75744,
                       -10.93206, 0.05133, -0.55109, -0.10201, 2010)

        elif ref_frame == Reference.ITRF08:
            return cls(1.00370, 0.00079, -1.91111, -0.00060, -0.54397, -0.00134, -26.78138, -0.06667, 0.42027, 0.75744,
                       -10.93206, 0.05133, 0.38891, -0.10201, 2010)

        elif ref_frame == Reference.ITRF14:
            return cls(1.00530, 0.00079, -1.90921, -0.00060, -0.54157, -0.00144, -26.78138, -0.06667, 0.42027, 0.75744,
                       -10.93206, 0.05133, 0.36891, -0.07201, 2010)

        else:
            raise KeyError(ref_frame)


@dataclass(frozen=True)
class VerticalGridShiftFactory(Factory):
    grid_shift: VerticalDatum

    @property
    def grid_shift_file(self):
        if self.grid_shift == VerticalDatum.CGG2013A:
            return "ca_nrc_CGG2013an83.tif"
        elif self.grid_shift == VerticalDatum.CGG2013:
            return "ca_nrc_CGG2013n83.tif"
        elif self.grid_shift == VerticalDatum.HT2_2010v70:
            return "ca_nrc_HT2_2010v70.tif"
        else:
            raise KeyError("Tried to get grid shift file for unknown grid.")

    @property
    def proj_str(self):
        if self.grid_shift is VerticalDatum.WGS84:
            return "+proj=noop"
        if self.grid_shift is VerticalDatum.GRS80:
            return "+proj=noop"
        else:
            return f"+inv +proj=vgridshift +grids={self.grid_shift_file} +multiplier=1"
