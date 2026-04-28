"""Ejecuta todas las combinaciones y muestra resultados basicos."""

#from __future__ import annotations
import pandas as pd

# from functions import (
#     in0_out0,
#     in0_out1,
#     in0_out2,
#     in1_out0,
#     in1_out1,
#     in1_out2,
#     in2_out0,
#     in2_out1,
#     in2_out2,
#     in3_out0,
#     in3_out1,
#     in3_out2,
# )


def main():
    # print("in0_out0 ->", in0_out0())
    # print("in0_out1 ->", in0_out1())
    # print("in0_out2 ->", in0_out2())

    # print("in1_out0 ->", in1_out0("hola"))
    # print("in1_out1 ->", in1_out1(123))
    # print("in1_out2 ->", in1_out2("abcd"))

    # print("in2_out0 ->", in2_out0(2, 3))
    # print("in2_out1 ->", in2_out1(2, 3))
    # print("in2_out2 ->", in2_out2("x", "y"))

    # print("in3_out0 ->", in3_out0(2, 3, 4))
    # print("in3_out1 ->", in3_out1(2, 3, 4))
    # try:
    #     status, df = in3_out2(1, 2, 3)
    #     print("in3_out2 ->", status)
    #     print(df)
    #     print("final")
    # except RuntimeError as exc:
    # 
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    # Devolver 0 y el DataFrame
    return 0, df


if __name__ == "__main__":
    status, df = main()
    print(status)
    print(df)
