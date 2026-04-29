"""Ejecuta todas las combinaciones y muestra resultados basicos."""

from __future__ import annotations
#import pandas as pd

from functions import (
    in0_out0,
    in0_out1,
    in0_out2,
    in1_out0,
    in1_out1,
    in1_out2,
    in2_out0,
    in2_out1,
    in2_out2,
    in3_out0,
    in3_out1,
    in3_out2,
)


def main()->None:
    print("in0_out0 ->", in0_out0())
    print("in0_out1 ->", in0_out1())
    print("in0_out2 ->", in0_out2())

    print("in1_out0 ->", in1_out0("hola"))
    print("in1_out1 ->", in1_out1(123))
    print("in1_out2 ->", in1_out2("abcd"))

    print("in2_out0 ->", in2_out0(2, 3))
    print("in2_out1 ->", in2_out1(2, 3))
    print("in2_out2 ->", in2_out2("x", "y"))

    print("in3_out0 ->", in3_out0(2, 3, 4))
    print("in3_out1 ->", in3_out1(2, 3, 4))


if __name__ == "__main__":
    main()

# def crear_df(n=200, seed=42):
#     import pandas as pd
#     import numpy as np

#     np.random.seed(seed)
#     ids = range(1, n+1)
#     fechas = pd.date_range("2020-01-01", periods=n, freq="D")
#     valores = np.random.randn(n)
#     categorias = np.random.choice(["A", "B", "C", "D"], size=n, p=[0.4, 0.3, 0.2, 0.1])
#     booleanos = np.random.choice([True, False], size=n)

#     df = pd.DataFrame({
#         "id": ids,
#         "fecha": fechas,
#         "valor": valores,
#         "categoria": categorias,
#         "activo": booleanos
#     })

#     return 0, df
