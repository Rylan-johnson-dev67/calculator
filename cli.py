"""Command-line interface for the calculator package."""

import argparse
import sys
import math
from calculator import compute


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="calculator", description="Simple calculator CLI"
    )
    parser.add_argument("op", help="operation (add, sub, mul, div or + - * /)")
    parser.add_argument("a", type=float, help="first operand")
    parser.add_argument("b", type=float, help="second operand")
    args = parser.parse_args(argv)

    try:
        result = compute(args.op, args.a, args.b)
    except Exception as e:
        print(f"Error: {e}")
        return 2

    # Print integer result without decimal when appropriate (use isclose for FP safety)
    try:
        if math.isclose(result, round(result), rel_tol=0, abs_tol=1e-9):
            print(int(round(result)))
        else:
            print(result)
    except Exception:
        # Fallback: just print raw result
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
