"""Funciones de prueba que cubren todas las combinaciones de entradas (0-3)
y salidas (0-2) con el formato solicitado.

Reglas:
- 0-3 parametros de entrada.
- 0-2 valores de retorno.
- Si hay retorno, el primer valor es int (estado), y el segundo (si existe)
  es un detalle: dict, int, str o pandas.DataFrame.
"""

from __future__ import annotations

from typing import Any


# 0 entradas ---------------------------------------------------------------

def in0_out0() -> None:
    """0 entradas, 0 salidas."""
    _ = sum([1, 2, 3])


def in0_out1() -> int:
    """0 entradas, 1 salida (estado)."""
    return 1


def in0_out2() -> tuple[int, dict[str, Any]]:
    """0 entradas, 2 salidas (estado, detalle dict)."""
    detalle = {"message": "ok", "items": [1, 2, 3]}
    return 1, detalle


# 1 entrada ----------------------------------------------------------------

def in1_out0(value: int | float | str) -> None:
    """1 entrada, 0 salidas."""
    _ = str(value).upper()


def in1_out1(value: Any) -> int:
    """1 entrada, 1 salida (estado)."""
    return 1 if value is not None else 0


def in1_out2(value: Any) -> tuple[int, int]:
    """1 entrada, 2 salidas (estado, detalle int)."""
    if value is None:
        return 0, 0
    if isinstance(value, (int, float)):
        return 1, int(value)
    return 1, len(str(value))


# 2 entradas ---------------------------------------------------------------

def in2_out0(a: int | float, b: int | float) -> None:
    """2 entradas, 0 salidas."""
    _ = a + b


def in2_out1(a: Any, b: Any) -> int:
    """2 entradas, 1 salida (estado)."""
    return 1 if a is not None and b is not None else 0


def in2_out2(a: Any, b: Any) -> tuple[int, str]:
    """2 entradas, 2 salidas (estado, detalle str)."""
    if a is None or b is None:
        return 0, "missing"
    return 1, f"a={a}, b={b}"


# 3 entradas ---------------------------------------------------------------

def in3_out0(a: int, b: int, c: int) -> None:
    """3 entradas, 0 salidas."""
    _ = a * b * c


def in3_out1(a: Any, b: Any, c: Any) -> int:
    """3 entradas, 1 salida (estado)."""
    return 1 if all(v is not None for v in (a, b, c)) else 0


def in3_out2(a: Any, b: Any, c: Any) -> tuple[int, "pandas.DataFrame"]:
    """3 entradas, 2 salidas (estado, detalle DataFrame)."""
    try:
        import pandas as pd
    except ImportError as exc:  # pragma: no cover - depende del entorno
        raise RuntimeError("pandas no esta instalado") from exc

    df = pd.DataFrame(
        [
            {"a": a, "b": b, "c": c},
            {"a": a, "b": b, "c": c},
        ]
    )
    return 1, df
