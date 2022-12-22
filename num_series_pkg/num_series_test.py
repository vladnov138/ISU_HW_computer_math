from math import exp, sin, cos, asin, acos

from num_series_pkg.num_series import *

EPS = 1e-10


def test_expand_exp_0():
    n = 0
    x = 0
    res = expand(x, n, func=expand_exp)
    ans = 1
    assert res == ans
    x = 10
    res = expand(x, n, func=expand_exp)
    assert res == ans


def test_expand_exp_1():
    n = 1
    x = 1
    res = expand(x, n, func=expand_exp)
    ans = 2
    assert res == ans
    x = -5
    ans = -4
    res = expand(x, n, func=expand_exp)
    assert res == ans


def test_expand_exp_2():
    n = 2
    x = -2
    res = expand(x, n, func=expand_exp)
    ans = 1
    assert res == ans
    x = 2
    ans = 5
    res = expand(x, n, func=expand_exp)
    assert res == ans


def test_expand_exp_3():
    n = 50
    x = 5
    res = expand(x, n, func=expand_exp)
    ans = exp(x)
    assert abs(res - ans) <= EPS


def test_expand_sin():
    n = 10
    x = 2
    res = expand(x, n, func=expand_sin)
    ans = sin(x)
    assert abs(res - ans) <= EPS


def test_expand_cos():
    n = 15
    x = 5
    res = expand(x, n, func=expand_cos)
    ans = cos(x)
    assert abs(res - ans) <= EPS


def test_expand_arcsin():
    n = 50
    x = 0.8
    res = expand(x, n, func=expand_arcsin)
    ans = asin(x)
    assert abs(res - ans) <= EPS


def test_expand_arccos():
    n = 30
    x = 0.3
    res = expand(x, n, func=expand_arccos)
    ans = acos(x)
    assert abs(res - ans) <= EPS
