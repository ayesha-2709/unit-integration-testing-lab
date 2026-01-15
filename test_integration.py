import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    b1, b2 = transfer(5000, 2000, 1000)
    assert b1 == 4000
    assert b2 == 3000


def test_transfer_failure():
    with pytest.raises(ValueError):
        transfer(1000, 2000, 3000)


def test_transfer_and_interest():
    b1, b2 = transfer(10000, 5000, 2000)
    final_amount = calculate_interest(b2, 10, 1)
    assert round(final_amount, 2) == 7700.00
