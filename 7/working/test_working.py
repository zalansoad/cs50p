from working import convert
import pytest

def test_invalidnumbers():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:76 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:06 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("13 AM - 5 PM")

def test_valid():
    assert convert("1:00 PM to 6:56 PM") == '13:00 to 18:56'
    assert convert("9 AM to 5 PM") == '09:00 to 17:00'


