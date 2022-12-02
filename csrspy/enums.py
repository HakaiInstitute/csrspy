from enum import Enum


class VerticalDatum(str, Enum):
    WGS84 = "wgs84"
    GRS80 = "grs80"
    CGG2013A = "cgg2013a"
    CGG2013 = "cgg2013"
    HT2_2010v70 = "ht2_2010v70"


class Reference(str, Enum):
    WGS84 = "wgs84"
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


class CoordType(str, Enum):
    GEOG = 'geog'
    CART = 'cart'
    UTM3 = 'utm3'
    UTM4 = 'utm4'
    UTM5 = 'utm5'
    UTM6 = 'utm6'
    UTM7 = 'utm7'
    UTM8 = 'utm8'
    UTM9 = 'utm9'
    UTM10 = 'utm10'
    UTM11 = 'utm11'
    UTM12 = 'utm12'
    UTM13 = 'utm13'
    UTM14 = 'utm14'
    UTM15 = 'utm15'
    UTM16 = 'utm16'
    UTM17 = 'utm17'
    UTM18 = 'utm18'
    UTM19 = 'utm19'
    UTM20 = 'utm20'
    UTM21 = 'utm21'
    UTM22 = 'utm22'
    UTM23 = 'utm23'
