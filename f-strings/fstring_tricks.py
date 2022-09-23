import datetime


def conversions():
    str_value = "other 🐶"

    # ascii
    print(f'{str_value!a}')

    # r is calling repr
    print(f'{str_value!r}')

    # str-int conversion
    print(f'{str_value!s}')


conversions()


def equals_debugging():
    str_value = "other 🐶"
    num_value = 123
    print(f'the value is {str_value}')
    print(f'{num_value = }')
    print(f'{num_value % 2 = }')


equals_debugging()


class MyClass:
    def __init__(self, set: str):
        self.set = set

    def __format__(self, format_spec) -> str:
        return self.set


def formatting():
    num_value = 123.456
    now = datetime.datetime.utcnow()
    print(f'{now=:%Y-%m-%d}')
    print(f'{num_value:.2f}')
    print(f'{MyClass():blah blah %%MYFORMAT%%}')

    nested_format = ".2f"
    print(f'{num_value:{nested_format}}')


formatting()