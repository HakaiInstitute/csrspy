import pytest

from csrspy import CSRSTransformer, enums


@pytest.mark.parametrize("transform_config,test_input,expected,xy_err,h_err", [
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.399, 5363983.346, 0.291),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2010, 'out': "geog"},
            (48.428421, -123.365646, 0),
            (48.42841703, -123.36562798, 0.291),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2010, 'out': "cart"},
            (48.428421, -123.365646, 0),
            (-2332023.027, -3541319.459, 4748619.680),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2007, 'out': "cart"},
            (48.428421, -123.365646, 0),
            (-2332023.056, -3541319.457, 4748619.672),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.NAD83CSRS, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2007, 'out': "cart"},
            (48.428421, -123.365646, 0),
            (-2332023.882, -3541318.287, 4748619.747),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF00, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2007, 'out': "cart"},
            (48.428421, -123.365646, 0),
            (-2332023.051, -3541319.451, 4748619.688),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF05, 's_crs': "EPSG:32610", 's_epoch': 2010, 't_epoch': 2014, 'out': "cart"},
            (472953.533, 5363982.768, -0.196),
            (-2332021.271, -3541321.343, 4748618.868),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF08, 's_crs': "+proj=cart +ellps=GRS80", 's_epoch': 2010, 't_epoch': 2014,
             'out': "utm10"},
            (-2332023.000, -3541319.000, 4748619.000),
            (472953.532, 5363982.764, -0.196),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': "EPSG:32610", 's_epoch': 2010, 't_epoch': 2014, 'out': "cart"},
            (472953.533, 5363982.768, -0.196),
            (-2332021.271, -3541321.345, 4748618.870),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF97, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.387, 5363983.385, 0.316),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF96, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.375, 5363983.346, 0.314),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF94, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.375, 5363983.346, 0.314),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF93, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.523, 5363983.350, 0.290),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF92, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.370, 5363983.347, 0.329),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF91, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.367, 5363983.337, 0.337),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF90, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.367, 5363983.351, 0.344),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF89, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.376, 5363983.359, 0.366),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF88, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.359, 5363983.402, 0.342),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2002, 't_vd': enums.Geoid.CGG2013A, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.272, 5363983.238, 18.969),
            0.001, 0.018
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2002, 't_vd': enums.Geoid.CGG2013, 'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.272, 5363983.238, 18.969),
            0.001, 0.018
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2002, 't_epoch': 2010, 't_vd': enums.Geoid.HT2_2010v70,
             'out': "utm10"},
            (48.428421, -123.365646, 0),
            (472952.339, 5363983.280, 18.806),
            0.001, 0.018
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': "EPSG:32610", 's_epoch': 2019.500, 't_epoch': 1997.000, 'out': "utm10"},
            (408125.360, 5635102.830, 2170.790),
            (408126.754, 5635102.429, 2170.925),
            0.001, 0.001
    ),
])
def test_csrs_transformer_forward(transform_config, test_input, expected, xy_err, h_err):
    trans = CSRSTransformer(**transform_config)
    out = list(trans.forward([test_input]))[0]

    assert pytest.approx(out[0], abs=xy_err) == expected[0]
    assert pytest.approx(out[1], abs=xy_err) == expected[1]
    assert pytest.approx(out[2], abs=h_err) == expected[2]


@pytest.mark.parametrize("transform_config,test_input,expected,xy_err,h_err", [
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2010, 'out': "utm10"},
            (472952.399, 5363983.346, 0.291),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2010, 'out': "geog"},
            (48.42841703, -123.36562798, 0.291),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2010, 'out': "cart"},
            (-2332023.027, -3541319.459, 4748619.680),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2007, 'out': "cart"},
            (-2332023.056, -3541319.457, 4748619.672),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.NAD83CSRS, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2007, 'out': "cart"},
            (-2332023.882, -3541318.287, 4748619.747),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF00, 's_crs': 4326, 's_epoch': 2010, 't_epoch': 2007, 'out': "cart"},
            (-2332023.051, -3541319.451, 4748619.688),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF05, 's_crs': "EPSG:32610", 's_epoch': 2010, 't_epoch': 2014, 'out': "cart"},
            (-2332021.271, -3541321.343, 4748618.868),
            (472953.533, 5363982.768, -0.196),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF08, 's_crs': "+proj=cart +ellps=GRS80", 's_epoch': 2010, 't_epoch': 2014,
             'out': "utm10"},
            (472953.532, 5363982.764, -0.196),
            (-2332023.000, -3541319.000, 4748619.000),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': "EPSG:32610", 's_epoch': 2010, 't_epoch': 2014, 'out': "cart"},
            (-2332021.271, -3541321.345, 4748618.870),
            (472953.533, 5363982.768, -0.196),
            0.001, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF97, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.387, 5363983.385, 0.316),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF96, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.375, 5363983.346, 0.314),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF94, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.375, 5363983.346, 0.314),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF93, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.523, 5363983.350, 0.290),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF92, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.370, 5363983.347, 0.329),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF91, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.367, 5363983.337, 0.337),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF90, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.367, 5363983.351, 0.344),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF89, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.376, 5363983.359, 0.366),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF88, 's_crs': 4326, 's_epoch': 2010, 'out': "utm10"},
            (472952.359, 5363983.402, 0.342),
            (48.428421, -123.365646, 0),
            1e-7, 0.001
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2002, 't_vd': enums.Geoid.CGG2013A, 'out': "utm10"},
            (472952.272, 5363983.238, 18.969),
            (48.428421, -123.365646, 0),
            1e-7, 0.018
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2002, 't_vd': enums.Geoid.CGG2013, 'out': "utm10"},
            (472952.272, 5363983.238, 18.969),
            (48.428421, -123.365646, 0),
            1e-7, 0.018
    ),
    (
            {'s_ref_frame': enums.Ref.ITRF14, 's_crs': 4326, 's_epoch': 2002, 't_epoch': 2010, 't_vd': enums.Geoid.HT2_2010v70,
             'out': "utm10"},
            (472952.339, 5363983.280, 18.806),
            (48.428421, -123.365646, 0),
            1e-7, 0.018
    ),
])
def test_csrs_transformer_backward(transform_config, test_input, expected, xy_err, h_err):
    trans = CSRSTransformer(**transform_config)
    out = list(trans.backward([test_input]))[0]

    assert pytest.approx(out[0], abs=xy_err) == expected[0]
    assert pytest.approx(out[1], abs=xy_err) == expected[1]
    assert pytest.approx(out[2], abs=h_err) == expected[2]
