import modules.matrix.matrix as mx
import modules.slae_by_gauss.slae_by_gauss as gauss


def test_1():
    a = [[2, 3], [4, 3]]
    b = [[2, 7]]
    x = gauss.solve_slae(a, b)
    res = mx.trans_matrix(mx.mul_matrix(a, mx.trans_matrix([mx.trans_matrix(x)[-1]])))
    assert res[0] == b[0]


def test_2():
    a = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
    b = [[15, -9, 5]]
    x = gauss.solve_slae(a, b)
    res = mx.trans_matrix(mx.mul_matrix(a, mx.trans_matrix([mx.trans_matrix(x)[-1]])))
    assert res[0] == b[0]


def test_3():
    a = [[4, 2, -1], [5, 3, -2], [3, 2, -3]]
    b = [[1, 2, 0]]
    x = gauss.solve_slae(a, b)
    res = mx.trans_matrix(mx.mul_matrix(a, mx.trans_matrix([mx.trans_matrix(x)[-1]])))
    assert res[0] == b[0]
