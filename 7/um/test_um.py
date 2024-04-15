import pytest

from um import count

def test_2():
    assert count("Um, thanks, um...") == 2

def test_0():
    assert count("Hello umbrella") == 0

def test_1():
    assert count("Um, thanks for the album.") == 1

