# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
# Unit test for twttr.py

from twttr import shorten


def test_shorten_vowels():
    assert shorten("AEIOU") == ""


def test_shorten_numbers():
    assert shorten("12345") == "12345"


def test_shorten_symbols():
    assert shorten("_,.#&@-") == "_,.#&@-"


def test_shorten_case_mix():
    assert shorten("mIsSiSsIpPi") == "msSSspP"