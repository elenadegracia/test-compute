def comprobar_venv():
    import sys
    import humanize

    print("Python:", sys.executable)
    print("humanize:", humanize.__version__)
