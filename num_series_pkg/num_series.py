from math import factorial, pi


def expand_exp(x, i):
    return x ** i / factorial(i)


def expand_cos(x, i, _a=0):
    return (-1) ** i * x ** (2 * i + _a) / factorial(2 * i + _a)


def expand_sin(x, i):
    return expand_cos(x, i, _a=1)


def expand_arcsin(x, i):
    check_arcx(x)
    return factorial(2 * i) / (4 ** i * factorial(i) ** 2 * (2 * i + 1)) * x ** (2 * i + 1)


def expand_arccos(x, i):
    check_arcx(x)
    return expand_arcsin(x, i)


def expand(x, n, func=expand_exp):
    res = sum([func(x, i) for i in range(n + 1)])
    return pi / 2 - res if func.__name__ == expand_arccos.__name__ \
        else res


def check_arcx(x):
    if abs(x) > 1:
        raise ValueError("Invalid value")
