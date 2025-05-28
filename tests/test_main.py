import pytest

from csrspy import CSRSTransformer
from csrspy.enums import CoordType, Reference, VerticalDatum


@pytest.mark.parametrize(
    ("transform_config", "test_input", "expected", "xy_err", "h_err"),
    [
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.399, 5363983.346, 0.291),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.GEOG,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (-123.36562798, 48.42841703, 0.291),
            1e-7,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.CART,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (-2332023.027, -3541319.459, 4748619.680),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.CART,
                "s_epoch": 2010,
                "t_epoch": 2007,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (-2332023.056, -3541319.457, 4748619.672),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF00,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.CART,
                "s_epoch": 2010,
                "t_epoch": 2007,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (-2332023.051, -3541319.451, 4748619.688),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF05,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.UTM10,
                "t_coords": CoordType.CART,
                "s_epoch": 2010,
                "t_epoch": 2014,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (472953.533, 5363982.768, -0.196),
            (-2332021.271, -3541321.343, 4748618.868),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF08,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.CART,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2014,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-2332023.000, -3541319.000, 4748619.000),
            (472953.532, 5363982.764, -0.196),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.UTM10,
                "t_coords": CoordType.CART,
                "s_epoch": 2010,
                "t_epoch": 2014,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (472953.533, 5363982.768, -0.196),
            (-2332021.271, -3541321.345, 4748618.870),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF97,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.387, 5363983.385, 0.316),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF96,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.375, 5363983.346, 0.314),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF94,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.375, 5363983.346, 0.314),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF93,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.523, 5363983.350, 0.290),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF92,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.370, 5363983.347, 0.329),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF91,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.367, 5363983.337, 0.337),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF90,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.367, 5363983.351, 0.344),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF89,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.376, 5363983.359, 0.366),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF88,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.359, 5363983.402, 0.342),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2002,
                "t_epoch": 2002,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.CGG2013A,
            },
            (-123.365646, 48.428421, 0),
            (472952.272, 5363983.238, 18.969),
            0.001,
            0.018,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2002,
                "t_epoch": 2002,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.CGG2013,
            },
            (-123.365646, 48.428421, 0),
            (472952.272, 5363983.238, 18.969),
            0.001,
            0.018,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2002,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.HT2_2010v70,
            },
            (-123.365646, 48.428421, 0),
            (472952.339, 5363983.280, 18.806),
            0.001,
            0.018,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.UTM10,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2019.500,
                "t_epoch": 1997.000,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (408125.360, 5635102.830, 2170.790),
            (408126.754, 5635102.429, 2170.925),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.UTM10,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010.00,
                "t_epoch": 2010.000,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (472953.533, 5363982.768, -0.196),
            (472954.864, 5363982.321, 0.095),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.CART,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010.00,
                "t_epoch": 2010.000,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-2332023.000, -3541319.000, 4748619.000),
            (472953.500, 5363982.747, -0.191),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF14,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010.00,
                "t_epoch": 2010.000,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (-123.365646, 48.428421, 0),
            (472952.399, 5363983.346, 0.291),
            0.001,
            0.001,
        ),
        (
            {
                "s_ref_frame": Reference.WGS84,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.GEOG,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2002,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.WGS84,
                "t_vd": VerticalDatum.HT2_2010v70,
            },
            (-123.365646, 48.428421, 0),
            (472952.339, 5363983.280, 18.806),
            0.001,
            0.018,
        ),
        (
            {
                "s_ref_frame": Reference.ITRF20,
                "t_ref_frame": Reference.NAD83CSRS,
                "s_coords": CoordType.UTM10,
                "t_coords": CoordType.UTM10,
                "s_epoch": 2010,
                "t_epoch": 2010,
                "s_vd": VerticalDatum.GRS80,
                "t_vd": VerticalDatum.GRS80,
            },
            (472952.399, 5363983.346, 0.291),
            (472953.729, 5363982.898, 0.580),
            0.001,
            0.001,
        ),
    ],
)
def test_csrs_transformer_itrf_to_nad83(
    transform_config, test_input, expected, xy_err, h_err
):
    trans = CSRSTransformer(**transform_config)
    out = next(iter(trans([test_input])))

    assert pytest.approx(out[0], abs=xy_err) == expected[0]
    assert pytest.approx(out[1], abs=xy_err) == expected[1]
    assert pytest.approx(out[2], abs=h_err) == expected[2]


@pytest.mark.parametrize(
    ("transform_config", "test_input", "expected", "xy_err", "h_err"),
    [
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.399, 5363983.346, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.GEOG,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (-123.36562798, 48.42841703, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.CART,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (-2332023.027, -3541319.459, 4748619.680),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.CART,
                "t_epoch": 2010,
                "s_epoch": 2007,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (-2332023.056, -3541319.457, 4748619.672),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF00,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.CART,
                "t_epoch": 2010,
                "s_epoch": 2007,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (-2332023.051, -3541319.451, 4748619.688),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF05,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.UTM10,
                "s_coords": CoordType.CART,
                "t_epoch": 2010,
                "s_epoch": 2014,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (-2332021.271, -3541321.343, 4748618.868),
            (472953.533, 5363982.768, -0.196),
            0.001,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF08,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.CART,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2014,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472953.532, 5363982.764, -0.196),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.UTM10,
                "s_coords": CoordType.CART,
                "t_epoch": 2010,
                "s_epoch": 2014,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (-2332021.271, -3541321.345, 4748618.870),
            (472953.533, 5363982.768, -0.196),
            0.001,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF97,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.387, 5363983.385, 0.316),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF96,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.375, 5363983.346, 0.314),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF94,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.375, 5363983.346, 0.314),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF93,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.523, 5363983.350, 0.290),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF92,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.370, 5363983.347, 0.329),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF91,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.367, 5363983.337, 0.337),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF90,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.367, 5363983.351, 0.344),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF89,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.376, 5363983.359, 0.366),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF88,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.359, 5363983.402, 0.342),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2002,
                "s_epoch": 2002,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.CGG2013A,
            },
            (472952.272, 5363983.238, 18.969),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.018,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2002,
                "s_epoch": 2002,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.CGG2013,
            },
            (472952.272, 5363983.238, 18.969),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.018,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2002,
                "s_epoch": 2010,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.HT2_2010v70,
            },
            (472952.339, 5363983.280, 18.806),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.018,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.UTM10,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2019.500,
                "s_epoch": 1997.000,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (408126.754, 5635102.429, 2170.925),
            (408125.360, 5635102.830, 2170.790),
            0.001,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.UTM10,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010.00,
                "s_epoch": 2010.000,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472954.864, 5363982.321, 0.095),
            (472953.533, 5363982.768, -0.196),
            0.001,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.CART,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010.00,
                "s_epoch": 2010.000,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472953.500, 5363982.747, -0.191),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF14,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010.00,
                "s_epoch": 2010.000,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.399, 5363983.346, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.WGS84,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.GEOG,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010.00,
                "s_epoch": 2010.000,
                "t_vd": VerticalDatum.WGS84,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.399, 5363983.346, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7,
            0.001,
        ),
        (
            {
                "t_ref_frame": Reference.ITRF20,
                "s_ref_frame": Reference.NAD83CSRS,
                "t_coords": CoordType.UTM10,
                "s_coords": CoordType.UTM10,
                "t_epoch": 2010.00,
                "s_epoch": 2010.000,
                "t_vd": VerticalDatum.GRS80,
                "s_vd": VerticalDatum.GRS80,
            },
            (472952.399, 5363983.346, 0.291),
            (472951.069, 5363983.794, 0.002),
            0.001,
            0.001,
        ),
    ],
)
def test_csrs_transformer_nad83_to_itrf(
    transform_config, test_input, expected, xy_err, h_err
):
    trans = CSRSTransformer(**transform_config)
    out = next(iter(trans([test_input])))

    assert pytest.approx(out[0], abs=xy_err) == expected[0]
    assert pytest.approx(out[1], abs=xy_err) == expected[1]
    assert pytest.approx(out[2], abs=h_err) == expected[2]


def test_csrs_transformer_nad83_ortho_to_ortho_transform():
    trans = CSRSTransformer(
        s_ref_frame=Reference.NAD83CSRS,
        t_ref_frame=Reference.NAD83CSRS,
        s_coords=CoordType.UTM10,
        t_coords=CoordType.UTM10,
        s_epoch=2002,
        t_epoch=2002,
        s_vd=VerticalDatum.CGG2013A,
        t_vd=VerticalDatum.HT2_2010v70,
    )
    out = next(iter(trans([(472952.272, 5363983.238, 18.969)])))

    assert pytest.approx(out[0], abs=0.001) == 472952.272
    assert pytest.approx(out[1], abs=0.001) == 5363983.238
    assert pytest.approx(out[2], abs=0.001) == 18.816


def test_csrs_transformer_nad83_vd_to_grs80_transform():
    trans = CSRSTransformer(
        s_ref_frame=Reference.NAD83CSRS,
        t_ref_frame=Reference.NAD83CSRS,
        s_coords=CoordType.UTM10,
        t_coords=CoordType.UTM10,
        s_epoch=2002,
        t_epoch=2002,
        s_vd=VerticalDatum.CGG2013A,
        t_vd=VerticalDatum.GRS80,
    )
    out = next(iter(trans([(472952.272, 5363983.238, 18.969)])))

    assert pytest.approx(out[0], abs=0.001) == 472952.272
    assert pytest.approx(out[1], abs=0.001) == 5363983.238
    assert pytest.approx(out[2], abs=0.01) == 0.302


def test_csrs_transformer_itrf_to_itrf_transform():
    trans = CSRSTransformer(
        s_ref_frame=Reference.ITRF14,
        t_ref_frame=Reference.ITRF00,
        s_coords=CoordType.GEOG,
        t_coords=CoordType.UTM10,
        s_epoch=2002,
        t_epoch=2000,
        s_vd=VerticalDatum.GRS80,
        t_vd=VerticalDatum.GRS80,
    )
    out = next(iter(trans([(-123.365646, 48.428421, 0)])))

    assert pytest.approx(out[0], abs=0.001) == 472951.082
    assert pytest.approx(out[1], abs=0.001) == 5363983.805
    assert pytest.approx(out[2], abs=0.001) == 0.001


@pytest.mark.parametrize(
    ("s_ref", "t_ref", "test_input", "expected", "err"),
    [
        # ITRF14 ECEF to NAD83CSRS ECEF
        (
            Reference.ITRF14,
            Reference.NAD83CSRS,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332022.174, -3541320.170, 4748618.925),
            0.01,
        ),
        # WGS84 ECEF to NAD83CSRS ECEF
        (
            Reference.WGS84,
            Reference.NAD83CSRS,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332022.174, -3541320.170, 4748618.925),
            0.01,
        ),
        # NAD83CSRS ECEF to ITRF14 ECEF
        (
            Reference.NAD83CSRS,
            Reference.ITRF14,
            (-2332022.174, -3541320.170, 4748618.925),
            (-2332023.000, -3541319.000, 4748619.000),
            0.01,
        ),
        # NAD83CSRS ECEF to WGS84 ECEF
        (
            Reference.NAD83CSRS,
            Reference.WGS84,
            (-2332022.174, -3541320.170, 4748618.925),
            (-2332023.000, -3541319.000, 4748619.000),
            0.01,
        ),
        # ITRF00 ECEF to ITRF14 ECEF
        (
            Reference.ITRF00,
            Reference.ITRF14,
            (-2332023.005, -3541319.006, 4748619.019),
            (-2332023.001, -3541319.000, 4748619.035),
            0.01,
        ),
        # ITRF14 ECEF to ITRF08 ECEF
        (
            Reference.ITRF14,
            Reference.ITRF08,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332022.998, -3541318.998, 4748619.002),
            0.01,
        ),
        # ITRF05 ECEF to ITRF20 ECEF
        (
            Reference.ITRF05,
            Reference.ITRF20,
            (-2332023.002, -3541319.003, 4748619.009),
            (-2332023.002, -3541319.002, 4748619.009),
            0.01,
        ),
    ],
)
def test_ecef_coordinate_transformations(s_ref, t_ref, test_input, expected, err):
    """Test ECEF (cartesian) coordinate transformations between different
    reference frames."""
    trans = CSRSTransformer(
        s_ref_frame=s_ref,
        t_ref_frame=t_ref,
        s_coords=CoordType.CART,
        t_coords=CoordType.CART,
        s_epoch=2010,
        t_epoch=2010,
        s_vd=VerticalDatum.GRS80 if s_ref != Reference.WGS84 else VerticalDatum.WGS84,
        t_vd=VerticalDatum.GRS80 if t_ref != Reference.WGS84 else VerticalDatum.WGS84,
    )
    out = next(iter(trans([test_input])))

    assert pytest.approx(out[0], abs=err) == expected[0]
    assert pytest.approx(out[1], abs=err) == expected[1]
    assert pytest.approx(out[2], abs=err) == expected[2]


@pytest.mark.parametrize(
    ("ref_frame", "test_input", "expected", "err"),
    [
        # ITRF14 ECEF to GEOG and back
        (
            Reference.ITRF14,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001,
        ),
        # WGS84 ECEF to GEOG and back
        (
            Reference.WGS84,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001,
        ),
        # ITRF00 ECEF to GEOG and back
        (
            Reference.ITRF00,
            (-2332023.005, -3541319.006, 4748619.019),
            (-2332023.005, -3541319.006, 4748619.019),
            0.001,
        ),
        # ITRF08 ECEF to GEOG and back
        (
            Reference.ITRF08,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001,
        ),
        # ITRF20 ECEF to GEOG and back
        (
            Reference.ITRF20,
            (-2332023.001, -3541319.001, 4748619.001),
            (-2332023.001, -3541319.001, 4748619.001),
            0.001,
        ),
    ],
)
def test_ecef_roundtrip_transformations(ref_frame, test_input, expected, err):
    """Test ECEF coordinates converted to geographic and back maintain precision."""
    # ECEF to Geographic
    trans_to_geog = CSRSTransformer(
        s_ref_frame=ref_frame,
        t_ref_frame=ref_frame,
        s_coords=CoordType.CART,
        t_coords=CoordType.GEOG,
        s_epoch=2010,
        t_epoch=2010,
        s_vd=VerticalDatum.GRS80
        if ref_frame != Reference.WGS84
        else VerticalDatum.WGS84,
        t_vd=VerticalDatum.GRS80
        if ref_frame != Reference.WGS84
        else VerticalDatum.WGS84,
    )

    # Geographic back to ECEF
    trans_to_cart = CSRSTransformer(
        s_ref_frame=ref_frame,
        t_ref_frame=ref_frame,
        s_coords=CoordType.GEOG,
        t_coords=CoordType.CART,
        s_epoch=2010,
        t_epoch=2010,
        s_vd=VerticalDatum.GRS80
        if ref_frame != Reference.WGS84
        else VerticalDatum.WGS84,
        t_vd=VerticalDatum.GRS80
        if ref_frame != Reference.WGS84
        else VerticalDatum.WGS84,
    )

    # Convert to geographic and back
    geog_coords = next(iter(trans_to_geog([test_input])))
    final_coords = next(iter(trans_to_cart([geog_coords])))

    assert pytest.approx(final_coords[0], abs=err) == expected[0]
    assert pytest.approx(final_coords[1], abs=err) == expected[1]
    assert pytest.approx(final_coords[2], abs=err) == expected[2]


@pytest.mark.parametrize(
    ("ref_frame", "epoch", "test_input", "expected", "err"),
    [
        # ITRF14 ECEF with epoch transformation
        (
            Reference.ITRF14,
            2007,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332022.202, -3541320.169, 4748618.915),
            0.1,
        ),
        # WGS84 ECEF with epoch transformation
        (
            Reference.WGS84,
            2014,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332022.136, -3541320.173, 4748618.937),
            0.1,
        ),
        # ITRF08 ECEF with epoch transformation
        (
            Reference.ITRF08,
            2014,
            (-2332023.000, -3541319.000, 4748619.000),
            (-2332022.138, -3541320.175, 4748618.935),
            0.1,
        ),
    ],
)
def test_ecef_epoch_transformations(ref_frame, epoch, test_input, expected, err):
    """Test ECEF coordinates with epoch transformations through NAD83CSRS."""
    trans = CSRSTransformer(
        s_ref_frame=ref_frame,
        t_ref_frame=Reference.NAD83CSRS,
        s_coords=CoordType.CART,
        t_coords=CoordType.CART,
        s_epoch=2010,
        t_epoch=epoch,
        s_vd=VerticalDatum.GRS80
        if ref_frame != Reference.WGS84
        else VerticalDatum.WGS84,
        t_vd=VerticalDatum.GRS80,
    )
    out = next(iter(trans([test_input])))

    assert pytest.approx(out[0], abs=err) == expected[0]
    assert pytest.approx(out[1], abs=err) == expected[1]
    assert pytest.approx(out[2], abs=err) == expected[2]
