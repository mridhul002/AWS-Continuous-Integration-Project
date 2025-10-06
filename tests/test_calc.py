import pytest
from app.calc import calculate

def test_add():
    assert calculate(2, 3, "add") == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(1, 0, "divide")

def test_invalid_op():
    with pytest.raises(ValueError):
        calculate(1, 2, "power")
