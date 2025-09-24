import subprocess
import sys
import runpy
from io import StringIO
import runpy
import sys
import math

from calculator.core import add, subtract, multiply, divide, compute


def test_large_integers():
    a = 10**18
    b = 10**18
    assert add(a, b) == a + b


def test_negative_numbers():
    assert subtract(-5, -3) == -2
    assert multiply(-2, 3) == -6


def test_float_precision():
    res = add(0.1, 0.2)
    # Not exact due to float, but close
    assert math.isclose(res, 0.3, rel_tol=1e-12, abs_tol=1e-12)


def test_divide_returns_float():
    assert isinstance(divide(5, 2), float)


def test_compute_alias_case_insensitive():
    assert compute("ADD", 1, 2) == 3


def run_module_capture(argv):
    old_argv = sys.argv[:] if hasattr(sys, "argv") else None
    old_stdout = sys.stdout
    try:
        sys.argv = ["python", *argv]
        out = StringIO()
        sys.stdout = out
        try:
            runpy.run_module("calculator", run_name="__main__")
        except SystemExit as e:
            # return both output and exit code
            return out.getvalue().strip(), getattr(e, "code", None)
        return out.getvalue().strip(), 0
    finally:
        if old_argv is not None:
            sys.argv = old_argv
        sys.stdout = old_stdout


def test_cli_invalid_op_exit_code():
    out, code = run_module_capture(["pow", "2", "3"])
    assert code == 2
    assert out.startswith("Error:")


def test_cli_divide_by_zero_exit_code():
    out, code = run_module_capture(["div", "1", "0"])
    assert code == 2
    assert "division by zero" in out
