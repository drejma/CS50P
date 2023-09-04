# https://cs50.harvard.edu/python/2022/psets/5/test_bank/
# Unit test for bank.py

from bank import value


def test_value_hello():
    assert value("Hello, John") == 0
    assert value("  hello, john  ") == 0


def test_value_h():
    assert value("Hi, John") == 20
    assert value("  howdy, john ") == 20


def test_value_other():
    assert value("What's up, John") == 100
    assert value("  good to see you, john  ") == 100
