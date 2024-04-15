from twttr import shorten

def test_argument():
    assert shorten("Hello World.") == "Hll Wrld."

def test_num():
    assert shorten("2") == "2"

def test_lower():
    assert shorten("ABCD") == "BCD"


