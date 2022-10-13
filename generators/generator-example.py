
def get_values():
    yield "hello"
    yield "world"
    yield 123


def example_get_values():
    gen = get_values()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))


def example_gen_com():
    squares = [x*x for x in range(5)]
    squares = (x * x for x in range(5))
    # sum squares
    sum_sqs = sum(x * x for x in range(5))


def another_generator():
    yield from (x*x for x in range(5))


if __name__ == '__main__':
    example_get_values()

    for x in get_values():
        print(x)

    print(next(another_generator()))