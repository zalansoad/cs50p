from seasons import Calculator


def test_valid():
    date = '1999-01-01'
    assert Calculator.conversion(date) == 'Thirteen million, two hundred sixty-nine thousand, six hundred minutes'

