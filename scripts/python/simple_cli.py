"""CLI simple para probar una funcion."""

from __future__ import annotations

import argparse

from functions import in2_out2


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejemplo sencillo")
    parser.add_argument("a", help="Valor a")
    parser.add_argument("b", help="Valor b")
    args = parser.parse_args()

    status, detail = in2_out2(args.a, args.b)
    print(f"status={status}")
    print(f"detail={detail}")


if __name__ == "__main__":
    main()
