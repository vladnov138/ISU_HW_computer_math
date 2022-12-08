from math import cos

from approximation_pkg.approximation import *

EPS = 1e-2


def test_lsm():
    a = [[2, 3], [3, 3], [4, 7]]
    b = [[7], [7], [3]]
    res = lsm(a, b)
    ans = [[4.68], [-2.06]]
    assert mx.equal_matrix_eps(ans, res, EPS)


def test_apprx_1():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [[1, 1], [3, 1], [5, 1]]
    res = apprx(data_xy, x)
    ans = [[1.66], [3.63], [5.60]]
    assert mx.equal_matrix_eps(ans, res, EPS)


def test_apprx_2():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [[1, 1], [3, 1], [5, 1]]
    res = apprx(data_xy, x, power=2)
    ans = [[2.08], [3.26], [5.46]]
    assert mx.equal_matrix_eps(ans, res, EPS)


def test_apprx_3():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [[1, 1], [3, 1], [5, 1]]
    res = apprx(data_xy, x, power=3)
    ans = [[2], [4], [2.16]]
    assert mx.equal_matrix_eps(ans, res, EPS)


def make_cos_func(x, power):
    """Returns func values"""
    func = [cos(x), x, 1]
    for i in range(2, power + 1):
        val = x ** i
        func.insert(0, val)
    return func


def test_apprx_4():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [[1, 1], [3, 1], [5, 1]]
    res = apprx(data_xy, x, power=1, func=make_cos_func)
    ans = [[2.07], [3.25], [5.68]]
    assert mx.equal_matrix_eps(ans, res, EPS)
