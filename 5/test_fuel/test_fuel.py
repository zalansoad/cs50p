from fuel import convert, gauge
import pytest


def test_xbigger():
    with pytest.raises(ValueError):
        convert("4/1")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_correctint():
    assert convert("1/4") == 25

def test_e():
    assert gauge(1) == "E"

def test_f():
    assert gauge(99) == "F"

def test_half():
    assert gauge(50) == "50%"


