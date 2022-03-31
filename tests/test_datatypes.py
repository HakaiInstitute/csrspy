from dataclasses import astuple

from csrspy import Coordinate


def test_coordinate():
    coord = Coordinate(1, 2, 3, 4)
    assert astuple(coord) == (1, 2, 3, 4)
    assert coord.x == 1
    assert coord.y == 2
    assert coord.z == 3
    assert coord.t == 4
