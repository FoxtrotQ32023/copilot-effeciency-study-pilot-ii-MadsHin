import pytest

from airport_finder import AirportFinder

test_input_path = "/workspaces/copilot-effeciency-study-pilot-ii-MadsHin/Assignment01/airlinehub.in"
test_output_path = "/workspaces/copilot-effeciency-study-pilot-ii-MadsHin/Assignment01/airlinehub.ans"

@pytest.fixture
def airport_finder_sut():
    sut = AirportFinder(test_input_path)
    return sut

@pytest.mark.parametrize("point_a, point_b, expected", [((0.0,0.0),(0.0,0.0), 0),((0.0,0.0),(3.0,0.0), 3),((0.0,0.0),(0.0,5.0), 5)] )
def test_calculate_distance(airport_finder_sut, point_a: tuple[float, float], point_b: tuple[float, float], expected: float):
    assert airport_finder_sut.calculate_distance(point_a, point_b) == expected


def test_find_airport_hubs(airport_finder_sut):
    assert airport_finder_sut.find_airport_hubs() == list[(3.20,-15.00),(3.20,-15.00)]