from validators import validate_name, validate_price
import pytest
@pytest.mark.parametrize("input, expected_status", [
        (None, 400),
        ("", 400),
        ("     ", 400),
        (999, 400),
        ("Rares", 200)
])

def test_validate_name(input, expected_status):
    result, status = validate_name(input)
    assert status == expected_status
    if result:
        assert result["status"] == status
    if status == 400:
        assert "eroare" in result
        
@pytest.mark.parametrize("input_price, expected_status", [
    (-10, 400),
    ("abc", 400),
    (None, 400),
    (19.99, 200),
    (100, 200),
])
def test_validate_price(input_price, expected_status):
    result, status = validate_price(input_price)
    assert status == expected_status
    if status == 400:
        assert "eroare" in result
        assert result["status"] == 400
    else:
        assert result is None
        