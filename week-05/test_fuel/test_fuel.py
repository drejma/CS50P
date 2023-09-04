# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
# Unit test for fuel.py

import pytest
import fuel


def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/3") == 33
    assert fuel.convert("2/3") == 67


def test_convert_value_error():
    with pytest.raises(ValueError):
        fuel.convert("cat/1")
        fuel.convert("1/2.5")
        fuel.convert("-2/-1")
        fuel.convert("2/1")


def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == f"50%"