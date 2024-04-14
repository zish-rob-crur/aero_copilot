try:
    import rich
except ImportError:
    color_print = print
else:

    def color_print(*args, **kwargs):
        rich.print(*args, **kwargs)

