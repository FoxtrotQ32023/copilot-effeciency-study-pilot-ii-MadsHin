import pytest
from pattern_matching import is_int, read_file, get_problems, solve_problem


def test_is_int():
    assert is_int("1") == True
    assert is_int("a") == False
    assert is_int("1a") == False
    assert is_int("a1") == False
    assert is_int("1 1") == False
    assert is_int("1 1 1") == False
    assert is_int("1 1 1 1") == False
    assert is_int("1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1 1 1 1 1 1") == False
    assert is_int("1 1 1 1 1 1 1 1 1 1 1 1 1 1") == False


test_list = ["3","n","hej", "dav", "dette er min streng", "3", "n", "hej", "dav", "dette er min streng2", "3", "n", "hej", "dav", "dette er min streng3"]
def test_get_problems():
    assert get_problems(test_list) == [["n","hej", "dav", "dette er min streng"], ["n", "hej", "dav", "dette er min streng2"], ["n", "hej", "dav", "dette er min streng3"]]


def test_solve_problem():
    # assert content of the file "stringmultimatching.in" is equal to the file "output.txt"
    solve_problem("stringmultimatching.in")
    assert read_file("output.ans") == read_file("stringmultimatching.ans")