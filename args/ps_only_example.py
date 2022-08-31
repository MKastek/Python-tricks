# Mimics maths
def power_mod(x, y, /, *, mod):
    return (x ** y) % mod


def check_truthy(x, /):  # should someone be able to pass this by name??
    if not x:
        raise ValueError(f"expected truthy object, got: {x}")
