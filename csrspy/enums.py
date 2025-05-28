"""Enums for CRS (Coordinate Reference System) definitions."""

from enum import Enum


class VerticalDatum(str, Enum):
    """Enum for vertical datums used in CRS definitions.

    This enum defines various vertical datums that can be used in geospatial
    applications.

    Attributes:
        WGS84: World Geodetic System 1984.
        GRS80: Geodetic Reference System 1980.
        CGG2013A: Canadian Geodetic Vertical Datum 2013 (adjusted).
        CGG2013: Canadian Geodetic Vertical Datum 2013.
        HT2_2010v70: Height Transformation version 70 from 2010.

    """

    WGS84 = "wgs84"
    GRS80 = "grs80"
    CGG2013A = "cgg2013a"
    CGG2013 = "cgg2013"
    HT2_2010v70 = "ht2_2010v70"


class Reference(str, Enum):
    """Enum for reference systems used in CRS definitions.

    This enum defines various reference systems that can be used in geospatial
    applications.

    Attributes:
        WGS84: World Geodetic System 1984.
        NAD83CSRS: North American Datum 1983 Canadian Spatial Reference System.
        ITRF88: International Terrestrial Reference Frame 1988.
        ITRF89: International Terrestrial Reference Frame 1989.
        ITRF90: International Terrestrial Reference Frame 1990.
        ITRF91: International Terrestrial Reference Frame 1991.
        ITRF92: International Terrestrial Reference Frame 1992.
        ITRF93: International Terrestrial Reference Frame 1993.
        ITRF94: International Terrestrial Reference Frame 1994.
        ITRF96: International Terrestrial Reference Frame 1996.
        ITRF97: International Terrestrial Reference Frame 1997.
        ITRF00: International Terrestrial Reference Frame 2000.
        ITRF05: International Terrestrial Reference Frame 2005.
        ITRF08: International Terrestrial Reference Frame 2008.
        ITRF14: International Terrestrial Reference Frame 2014.
        ITRF20: International Terrestrial Reference Frame 2020.

    """

    WGS84 = "wgs84"
    NAD83CSRS = "nad83csrs"
    ITRF88 = "itrf88"
    ITRF89 = "itrf89"
    ITRF90 = "itrf90"
    ITRF91 = "itrf91"
    ITRF92 = "itrf92"
    ITRF93 = "itrf93"
    ITRF94 = "itrf94"
    ITRF96 = "itrf96"
    ITRF97 = "itrf97"
    ITRF00 = "itrf00"
    ITRF05 = "itrf05"
    ITRF08 = "itrf08"
    ITRF14 = "itrf14"
    ITRF20 = "itrf20"


class CoordType(str, Enum):
    """Enum for coordinate types used in CRS definitions.

    This enum defines various coordinate systems that can be used in geospatial
    applications.

    Attributes:
        GEOG: Geographic coordinate system.
        CART: Cartesian coordinate system.
        UTM3: Universal Transverse Mercator zone 3.
        UTM4: Universal Transverse Mercator zone 4.
        UTM5: Universal Transverse Mercator zone 5.
        UTM6: Universal Transverse Mercator zone 6.
        UTM7: Universal Transverse Mercator zone 7.
        UTM8: Universal Transverse Mercator zone 8.
        UTM9: Universal Transverse Mercator zone 9.
        UTM10: Universal Transverse Mercator zone 10.
        UTM11: Universal Transverse Mercator zone 11.
        UTM12: Universal Transverse Mercator zone 12.
        UTM13: Universal Transverse Mercator zone 13.
        UTM14: Universal Transverse Mercator zone 14.
        UTM15: Universal Transverse Mercator zone 15.
        UTM16: Universal Transverse Mercator zone 16.
        UTM17: Universal Transverse Mercator zone 17.
        UTM18: Universal Transverse Mercator zone 18.
        UTM19: Universal Transverse Mercator zone 19.
        UTM20: Universal Transverse Mercator zone 20.
        UTM21: Universal Transverse Mercator zone 21.
        UTM22: Universal Transverse Mercator zone 22.
        UTM23: Universal Transverse Mercator zone 23.

    """

    GEOG = "geog"
    CART = "cart"
    UTM3 = "utm3"
    UTM4 = "utm4"
    UTM5 = "utm5"
    UTM6 = "utm6"
    UTM7 = "utm7"
    UTM8 = "utm8"
    UTM9 = "utm9"
    UTM10 = "utm10"
    UTM11 = "utm11"
    UTM12 = "utm12"
    UTM13 = "utm13"
    UTM14 = "utm14"
    UTM15 = "utm15"
    UTM16 = "utm16"
    UTM17 = "utm17"
    UTM18 = "utm18"
    UTM19 = "utm19"
    UTM20 = "utm20"
    UTM21 = "utm21"
    UTM22 = "utm22"
    UTM23 = "utm23"
