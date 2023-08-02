from csrspy.factories import HelmertFactory


def test_helmert_from_ref_string():
    assert isinstance(HelmertFactory.from_ref_frame("itrf14"), HelmertFactory)
