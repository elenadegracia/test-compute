"""Demostracion de salida DataFrame."""

from __future__ import annotations

from functions import in3_out2


def main() -> None:
    status, df = in3_out2("uno", "dos", "tres")
    print("status=", status)
    print(df)


if __name__ == "__main__":
    main()
