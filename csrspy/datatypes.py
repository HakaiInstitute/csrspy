from dataclasses import astuple, dataclass
from enum import Enum
from typing import Optional, Tuple

CoordTuple = Tuple[float, float, float, float]


@dataclass
class Coordinate:
    x: float
    y: float
    z: float
    t: float = None

    @classmethod
    def from_tuple(cls, tup: CoordTuple):
        return cls(*tup)

    def to_tuple(self, t: Optional[float] = None) -> tuple[float, ...]:
        self.t = t if t is not None else self.t
        return astuple(self)


class Geoid(str, Enum):
    CGG2013A = "cgg2013a"
    CGG2013 = "cgg2013"
    HT2_2010v70 = "ht2_2010v70"
    HT2_2002v70 = "ht2_2002v70"
    HT2_1997 = "ht2_1997"


class Ref(str, Enum):
    NAD83CSRS = 'nad83csrs'
    ITRF88 = 'itrf88'
    ITRF89 = 'itrf89'
    ITRF90 = 'itrf90'
    ITRF91 = 'itrf91'
    ITRF92 = 'itrf92'
    ITRF93 = 'itrf93'
    ITRF94 = 'itrf94'
    ITRF96 = 'itrf96'
    ITRF97 = 'itrf97'
    ITRF00 = 'itrf00'
    ITRF05 = 'itrf05'
    ITRF08 = 'itrf08'
    ITRF14 = 'itrf14'
