# https://cs50.harvard.edu/python/2022/psets/5/test_plates/
# Unit test for plates.py

from plates import is_valid


def test_is_valid_len():
    assert is_valid("A") == False
    assert is_valid("AAAA123") == False
    assert is_valid("AAA123") == True


def test_is_valid_letters():
    assert is_valid("123") == False
    assert is_valid("A123") == False
    assert is_valid("AA123") == True


def test_is_valid_symbols():
    assert is_valid("AA.23") == False
    assert is_valid("AA#&3") == False


def test_is_valid_zero():
    assert is_valid("AA012") == False


def test_is_valid_numbers():
    assert is_valid("AA12B") == False