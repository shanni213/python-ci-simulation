import pytest
from src.logic import convert_currency


def test_standard_conversion():
    assert convert_currency(100, "ILS", "USD") == 27.17


def test_same_currency():
    assert convert_currency(50, "USD", "USD") == 50.0


def test_zero_amount():
    assert convert_currency(0, "EUR", "ILS") == 0.0


def test_negative_amount_raises_error():
    with pytest.raises(ValueError, match="סכום לא יכול להיות שלילי"):
        convert_currency(-10, "ILS", "USD")


def test_unsupported_currency_raises_error():
    with pytest.raises(ValueError, match="מטבע לא נתמך"):
        convert_currency(100.0, "XYZ", "USD")


def test_case_insensitivity():
    assert convert_currency(100, "ils", "uSd") == 27.17


def test_whitespace_handling():
    assert convert_currency(100, "  ILS  ", "USD ") == 27.17


def test_decimal_rounding():
    assert convert_currency(10, "EUR", "ILS") == 40.0
