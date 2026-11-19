def comprobar_venv(**kwargs):
    from importlib.metadata import version

    actual = version("humanize")
    if actual != "4.11.0":
        raise RuntimeError(
            f"Venv incorrecto: humanize={actual}; esperado=4.11.0"
        )

    return {"humanize": actual}
