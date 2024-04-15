from numb3rs import validate

def test_range():
    assert validate("127.0.0.1") == True
    assert validate("56.76.65") == False
    assert validate("75.456.76.65") == False
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
    assert validate("0.5.255.255") == True
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("cat") == False
    assert validate(" 255.255.255.255") == False



