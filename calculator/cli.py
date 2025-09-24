"""Package-level CLI for calculator."""

import argparse
import math
from .core import compute


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="calculator", description="Simple calculator CLI"
    )
    parser.add_argument(
        "op",
        help="operation (add, sub, mul, div or + - * /) or 'repl' for interactive mode",
    )
    parser.add_argument("a", type=float, nargs="?", help="first operand")
    parser.add_argument("b", type=float, nargs="?", help="second operand")
    args = parser.parse_args(argv)

    if args.op == "repl":
        return repl()

    if args.a is None or args.b is None:
        print("Error: op requires two numeric arguments")
        return 2

    try:
        result = compute(args.op, args.a, args.b)
    except Exception as e:
        print(f"Error: {e}")
        return 2

    try:
        if math.isclose(result, round(result), rel_tol=0, abs_tol=1e-9):
            print(int(round(result)))
        else:
            print(result)
    except Exception:
        print(result)
    return 0


def repl():
    """Simple REPL for quick calculations. Type 'exit' or Ctrl-D to quit."""
    print("calculator REPL. Enter: <op> <a> <b> e.g. add 2 3")
    try:
        while True:
            try:
                line = input("> ").strip()
            except EOFError:
                break
            if not line:
                continue
            if line.lower() in ("exit", "quit"):
                break
            parts = line.split()
            if len(parts) != 3:
                print("Usage: <op> <a> <b>")
                continue
            op, a_s, b_s = parts
            try:
                a = float(a_s)
                b = float(b_s)
            except ValueError:
                print("Error: operands must be numbers")
                continue
            try:
                res = compute(op, a, b)
                if math.isclose(res, round(res), rel_tol=0, abs_tol=1e-9):
                    print(int(round(res)))
                else:
                    print(res)
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        pass
    print()  # newline
    return 0
