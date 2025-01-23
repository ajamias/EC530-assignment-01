import pytest
from assignment_01.get_closest_points import (
    get_closest_points,
    InvalidInputException,
)


def test_get_closest_points():
    list_1 = [
        (0, 0),
        (45, 90),
        (-45, 45),
    ]

    list_2 = [
        (90, 90),
        (-90, -90),
    ]

    output = get_closest_points(list_1, list_2)
    assert output == [0, 0, 1]


def test_empty_lists():
    list_1 = []

    list_2 = [(0, 0)]

    with pytest.raises(InvalidInputException):
        get_closest_points(list_1, list_1)
        get_closest_points(list_1, list_2)
        get_closest_points(list_2, list_1)


def test_invalid_input_type():
    not_a_list_1 = ()

    not_a_list_2 = {}

    with pytest.raises(InvalidInputException):
        get_closest_points(not_a_list_1, not_a_list_2)


def test_invalid_coordinates():
    list_1 = [
        (-180, 180),
        (-180, 0),
        (90, 180),
        (0, 0)
    ]

    list_2 = [
        (12, 34),
        (56, -78),
        (-9, 10),
        (100, -100)
    ]

    with pytest.raises(InvalidInputException):
        get_closest_points(list_1, list_2)
