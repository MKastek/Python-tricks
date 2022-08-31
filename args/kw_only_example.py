def g(a, b, *, kw_only):
    print(f'{a=}, {b=}, {kw_only=}')

#Everything after *, *args is keyword argument

def g(a, b, *args, kw_only):
    if args:
        raise ValueError(f"unexpected positional arguments: {args}")
    print(f'{a=}, {b=}, {kw_only}')