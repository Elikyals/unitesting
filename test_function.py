import pytest
from script import changeUppercase


def test_for_uppercase():
    assert changeUppercase("Eliyahu") == "ELIYAHU"


def test_other_for_uppercase():
    test_argument = "Lum"
    expected = "LUM"
    actual = changeUppercase(test_argument)
    message = f"changeUppercase('lum') should return {expected}, but it actually returned {actual}"
    assert actual == expected, message
