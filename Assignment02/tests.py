import pytest
from pattern_matching import is_int, read_file


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

