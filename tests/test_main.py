import pytest

from csrspy import CSRSTransformer
from csrspy.enums import CoordType, Reference, VerticalDatum


@pytest.mark.parametrize("transform_config,test_input,expected,xy_err,h_err", [
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.399, 5363983.346, 0.291),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.GEOG,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (-123.36562798, 48.42841703, 0.291),
            1e-7, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.CART,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (-2332023.027, -3541319.459, 4748619.680),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.CART,
                's_epoch': 2010, 't_epoch': 2007,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (-2332023.056, -3541319.457, 4748619.672),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF00, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.CART,
                's_epoch': 2010, 't_epoch': 2007,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (-2332023.051, -3541319.451, 4748619.688),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF05, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.UTM10, 't_coords': CoordType.CART,
                's_epoch': 2010, 't_epoch': 2014,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (472953.533, 5363982.768, -0.196),
            (-2332021.271, -3541321.343, 4748618.868),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF08, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.CART, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2014,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-2332023.000, -3541319.000, 4748619.000),
            (472953.532, 5363982.764, -0.196),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.UTM10, 't_coords': CoordType.CART,
                's_epoch': 2010, 't_epoch': 2014,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (472953.533, 5363982.768, -0.196),
            (-2332021.271, -3541321.345, 4748618.870),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF97, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.387, 5363983.385, 0.316),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF96, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.375, 5363983.346, 0.314),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF94, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.375, 5363983.346, 0.314),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF93, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.523, 5363983.350, 0.290),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF92, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.370, 5363983.347, 0.329),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF91, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.367, 5363983.337, 0.337),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF90, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.367, 5363983.351, 0.344),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF89, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.376, 5363983.359, 0.366),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF88, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.359, 5363983.402, 0.342),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2002, 't_epoch': 2002,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.CGG2013A
            },
            (-123.365646, 48.428421, 0),
            (472952.272, 5363983.238, 18.969),
            0.001, 0.018
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2002, 't_epoch': 2002,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.CGG2013
            },
            (-123.365646, 48.428421, 0),
            (472952.272, 5363983.238, 18.969),
            0.001, 0.018
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2002, 't_epoch': 2010,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.HT2_2010v70
            },
            (-123.365646, 48.428421, 0),
            (472952.339, 5363983.280, 18.806),
            0.001, 0.018
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.UTM10, 't_coords': CoordType.UTM10,
                's_epoch': 2019.500, 't_epoch': 1997.000,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (408125.360, 5635102.830, 2170.790),
            (408126.754, 5635102.429, 2170.925),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.UTM10, 't_coords': CoordType.UTM10,
                's_epoch': 2010.00, 't_epoch': 2010.000,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (472953.533, 5363982.768, -0.196),
            (472954.864, 5363982.321, 0.095),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.CART, 't_coords': CoordType.UTM10,
                's_epoch': 2010.00, 't_epoch': 2010.000,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-2332023.000, -3541319.000, 4748619.000),
            (472953.500, 5363982.747, -0.191),
            0.001, 0.001
    ),
    (
            {
                "s_ref_frame": Reference.ITRF14, 't_ref_frame': Reference.NAD83CSRS,
                's_coords': CoordType.GEOG, 't_coords': CoordType.UTM10,
                's_epoch': 2010.00, 't_epoch': 2010.000,
                's_vd': VerticalDatum.GRS80, 't_vd': VerticalDatum.GRS80
            },
            (-123.365646, 48.428421, 0),
            (472952.399, 5363983.346, 0.291),
            0.001, 0.001
    ),
])
def test_csrs_transformer_itrf_to_nad83(transform_config, test_input, expected, xy_err, h_err):
    trans = CSRSTransformer(**transform_config)
    out = list(trans([test_input]))[0]

    assert pytest.approx(out[0], abs=xy_err) == expected[0]
    assert pytest.approx(out[1], abs=xy_err) == expected[1]
    assert pytest.approx(out[2], abs=h_err) == expected[2]


@pytest.mark.parametrize("transform_config,test_input,expected,xy_err,h_err", [
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.399, 5363983.346, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.GEOG,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (-123.36562798, 48.42841703, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.CART,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (-2332023.027, -3541319.459, 4748619.680),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.CART,
                't_epoch': 2010, 's_epoch': 2007,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (-2332023.056, -3541319.457, 4748619.672),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF00, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.CART,
                't_epoch': 2010, 's_epoch': 2007,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (-2332023.051, -3541319.451, 4748619.688),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF05, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.UTM10, 's_coords': CoordType.CART,
                't_epoch': 2010, 's_epoch': 2014,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (-2332021.271, -3541321.343, 4748618.868),
            (472953.533, 5363982.768, -0.196),
            0.001, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF08, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.CART, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2014,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472953.532, 5363982.764, -0.196),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.UTM10, 's_coords': CoordType.CART,
                't_epoch': 2010, 's_epoch': 2014,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (-2332021.271, -3541321.345, 4748618.870),
            (472953.533, 5363982.768, -0.196),
            0.001, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF97, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.387, 5363983.385, 0.316),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF96, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.375, 5363983.346, 0.314),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF94, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.375, 5363983.346, 0.314),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF93, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.523, 5363983.350, 0.290),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF92, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.370, 5363983.347, 0.329),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF91, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.367, 5363983.337, 0.337),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF90, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.367, 5363983.351, 0.344),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF89, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.376, 5363983.359, 0.366),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF88, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.359, 5363983.402, 0.342),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2002, 's_epoch': 2002,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.CGG2013A
            },
            (472952.272, 5363983.238, 18.969),
            (-123.365646, 48.428421, 0),
            1e-7, 0.018
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2002, 's_epoch': 2002,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.CGG2013
            },
            (472952.272, 5363983.238, 18.969),
            (-123.365646, 48.428421, 0),
            1e-7, 0.018
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2002, 's_epoch': 2010,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.HT2_2010v70
            },
            (472952.339, 5363983.280, 18.806),
            (-123.365646, 48.428421, 0),
            1e-7, 0.018
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.UTM10, 's_coords': CoordType.UTM10,
                't_epoch': 2019.500, 's_epoch': 1997.000,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (408126.754, 5635102.429, 2170.925),
            (408125.360, 5635102.830, 2170.790),
            0.001, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.UTM10, 's_coords': CoordType.UTM10,
                't_epoch': 2010.00, 's_epoch': 2010.000,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472954.864, 5363982.321, 0.095),
            (472953.533, 5363982.768, -0.196),
            0.001, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.CART, 's_coords': CoordType.UTM10,
                't_epoch': 2010.00, 's_epoch': 2010.000,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472953.500, 5363982.747, -0.191),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001, 0.001
    ),
    (
            {
                "t_ref_frame": Reference.ITRF14, 's_ref_frame': Reference.NAD83CSRS,
                't_coords': CoordType.GEOG, 's_coords': CoordType.UTM10,
                't_epoch': 2010.00, 's_epoch': 2010.000,
                't_vd': VerticalDatum.GRS80, 's_vd': VerticalDatum.GRS80
            },
            (472952.399, 5363983.346, 0.291),
            (-123.365646, 48.428421, 0),
            1e-7, 0.001
    ),
])
def test_csrs_transformer_nad83_to_itrf(transform_config, test_input, expected, xy_err, h_err):
    trans = CSRSTransformer(**transform_config)
    out = list(trans([test_input]))[0]

    assert pytest.approx(out[0], abs=xy_err) == expected[0]
    assert pytest.approx(out[1], abs=xy_err) == expected[1]
    assert pytest.approx(out[2], abs=h_err) == expected[2]


def test_csrs_transformer_nad83_ortho_to_ortho_transform():
    trans = CSRSTransformer(s_ref_frame=Reference.NAD83CSRS, t_ref_frame=Reference.NAD83CSRS,
                            s_coords=CoordType.UTM10, t_coords=CoordType.UTM10,
                            s_epoch=2002, t_epoch=2002,
                            s_vd=VerticalDatum.CGG2013A, t_vd=VerticalDatum.HT2_2010v70
                            )
    out = list(trans([(472952.272, 5363983.238, 18.969)]))[0]

    assert pytest.approx(out[0], abs=0.001) == 472952.272
    assert pytest.approx(out[1], abs=0.001) == 5363983.238
    assert pytest.approx(out[2], abs=0.001) == 18.816


def test_csrs_transformer_nad83_vd_to_grs80_transform():
    trans = CSRSTransformer(s_ref_frame=Reference.NAD83CSRS, t_ref_frame=Reference.NAD83CSRS,
                            s_coords=CoordType.UTM10, t_coords=CoordType.UTM10,
                            s_epoch=2002, t_epoch=2002,
                            s_vd=VerticalDatum.CGG2013A, t_vd=VerticalDatum.GRS80
                            )
    out = list(trans([(472952.272, 5363983.238, 18.969)]))[0]

    assert pytest.approx(out[0], abs=0.001) == 472952.272
    assert pytest.approx(out[1], abs=0.001) == 5363983.238
    assert pytest.approx(out[2], abs=0.01) == 0.302


def test_csrs_transformer_itrf_to_itrf_transform():
    trans = CSRSTransformer(s_ref_frame=Reference.ITRF14, t_ref_frame=Reference.ITRF00,
                            s_coords=CoordType.GEOG, t_coords=CoordType.UTM10,
                            s_epoch=2002, t_epoch=2000,
                            s_vd=VerticalDatum.GRS80, t_vd=VerticalDatum.GRS80
                            )
    out = list(trans([(-123.365646, 48.428421, 0)]))[0]

    assert pytest.approx(out[0], abs=0.001) == 472951.082
    assert pytest.approx(out[1], abs=0.001) == 5363983.805
    assert pytest.approx(out[2], abs=0.001) == 0.001
