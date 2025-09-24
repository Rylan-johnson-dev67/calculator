from hypothesis import given
import hypothesis.strategies as st
from calculator.core import add, subtract, multiply, divide
import math


@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)


@given(st.integers(), st.integers())
def test_subtraction_inverse(a, b):
    assert subtract(a, b) + b == a


# Restrict floats to avoid overflow in operations
float_bounds = dict(allow_nan=False, allow_infinity=False, min_value=-1e100, max_value=1e100)


@given(st.floats(**float_bounds), st.floats(**float_bounds))
def test_multiplication_commutative(a, b):
    assert multiply(a, b) == multiply(b, a)


@given(st.floats(**float_bounds), st.floats(**float_bounds))
def test_division_multiplicative_inverse(a, b):
    # avoid zero divisor
    if b == 0:
        return
    q = divide(a, b)
    # skip pathological cases where intermediate quotient is not finite
    if not math.isfinite(q):
        return
    res = q * b
    assert math.isclose(res, a, rel_tol=1e-6, abs_tol=1e-6)
