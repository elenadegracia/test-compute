"""Script de prueba que falla con ValueError."""


def main() -> None:
    raise ValueError("valor invalido: prueba intencional")


if __name__ == "__main__":
    main()
