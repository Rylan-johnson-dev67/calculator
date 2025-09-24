import pytest
from calculator.core import add, subtract, multiply, divide, compute


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 2.5) == 10.0


def test_divide():
    assert divide(9, 3) == 3


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_compute_aliases():
    assert compute("+", 1, 2) == 3
    assert compute("add", 1, 2) == 3
    assert compute("mul", 3, 3) == 9
    assert compute("divide", 8, 2) == 4


def test_compute_invalid():
    with pytest.raises(ValueError):
        compute("pow", 2, 3)
