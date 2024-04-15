from bank import value

def test_0():
    assert value("Hello friend") == 0

def test_20():
    assert value("Howdy") == 20

def test_100():
    assert value("Good morning") == 100
