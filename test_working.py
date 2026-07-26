from working import convert
import pytest
def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_with_minutes():
    assert convert("10:30 PM to 8:45 AM") == "22:30 to 08:45"
def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
def test_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM" )
