from slae_gauss import *


def test_1():
    a = [[2, 3], [4, 3]]
    b = [2, 7]
    c = mx.trans_matrix(mx.create_new_row(mx.trans_matrix(a), b))
    x = mx.trans_matrix(solve_slae(c))
    res = mx.trans_matrix(mx.mul_matrix(a, x))
    assert res[0] == b


def test_2():
    a = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
    b = [15, -9, 5]
    c = mx.trans_matrix(mx.create_new_row(mx.trans_matrix(a), b))
    x = mx.trans_matrix(solve_slae(c))
    res = mx.trans_matrix(mx.mul_matrix(a, x))
    assert res[0] == b


def test_3():
    a = [[4, 2, -1], [5, 3, -2], [3, 2, -3]]
    b = [1, 2, 0]
    c = mx.trans_matrix(mx.create_new_row(mx.trans_matrix(a), b))
    x = mx.trans_matrix(solve_slae(c))
    res = mx.trans_matrix(mx.mul_matrix(a, x))
    assert res[0] == b
