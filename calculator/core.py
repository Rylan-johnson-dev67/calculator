"""Core calculator operations"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def compute(op: str, a: Number, b: Number) -> Number:
    """Compute result of operation op with operands a and b.

    op: one of '+', '-', '*', '/', 'add', 'sub', 'mul', 'div'
    """
    op = op.strip().lower()
    if op in ("+", "add"):
        return add(a, b)
    if op in ("-", "sub"):
        return subtract(a, b)
    if op in ("*", "x", "mul", "multiply"):
        return multiply(a, b)
    if op in ("/", "div", "divide"):
        return divide(a, b)
    raise ValueError(f"unsupported operation: {op}")
