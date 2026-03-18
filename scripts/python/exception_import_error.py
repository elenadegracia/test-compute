"""Script de prueba que falla con ImportError."""


def main() -> None:
    import modulo_que_no_existe  # type: ignore[import-not-found]

    _ = modulo_que_no_existe  # pragma: no cover


if __name__ == "__main__":
    main()
