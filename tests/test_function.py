import pytest
from src.data.script import changeUppercase


class TestForUppercase(object):
    def test_for_uppercase(self):
        assert changeUppercase("Eliyahu") == "ELIYAHU"

    def test_other_for_uppercase(self):
        test_argument = "Lum"
        expected = "LUM"
        actual = changeUppercase(test_argument)
        message = f"changeUppercase('lum') should return {expected}, but it actually returned {actual}"
        assert actual == expected, message
