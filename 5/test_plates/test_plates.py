from plates import is_valid

def test_maxchar():
    assert is_valid("ASDASDASDASD") == False
def test_minchar():
    assert is_valid("A") == False
def test_noprefzero():
    assert is_valid("CS05") == False
def test_numberend():
    assert is_valid("CS50P2") == False
def test_beginsalpha():
    assert is_valid("12") == False
def test_alphanum():
    assert is_valid("AA$.$") == False
def test_valid():
    assert is_valid("CS50") == True

