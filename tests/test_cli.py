import runpy
import sys
from io import StringIO


def run_module_capture(argv):
    old_argv = sys.argv[:] if hasattr(sys, "argv") else None
    old_stdout = sys.stdout
    try:
        sys.argv = ["python", *argv]
        out = StringIO()
        sys.stdout = out
        try:
            runpy.run_module("calculator", run_name="__main__")
        except SystemExit:
            # Module may call sys.exit(); ignore the exit but keep captured output
            pass
        return out.getvalue().strip()
    finally:
        if old_argv is not None:
            sys.argv = old_argv
        sys.stdout = old_stdout


def test_cli_add():
    out = run_module_capture(["add", "2", "3"])
    assert out == "5"


def test_cli_divide_float():
    out = run_module_capture(["div", "5", "2"])
    assert out == "2.5" or out == "5/2"
