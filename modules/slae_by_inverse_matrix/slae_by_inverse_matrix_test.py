import modules.matrix.matrix as mx
import slae_by_inverse_matrix as inv_m

EPS = 1e-10


def test_inverse_1():
    a = [[1, 2], [3, 4]]
    inverse_m = inv_m.get_inverse_matrix(a)
    res = mx.mul_matrix(a, inverse_m)
    identity = inv_m.get_identity_matrix(len(a))
    assert identity == res


def test_solve_slae_1():
    a = [[1, 2], [3, 4]]
    b = [[6], [8]]
    res = inv_m.solve_slae(a, b)
    assert mx.mul_matrix(a, res) == b


def test_solve_slae_2():
    a = [[2, 3], [4, 3]]
    b = [[2], [7]]
    res = mx.mul_matrix(a, inv_m.solve_slae(a, b))
    for i in range(len(res)):
        assert abs(res[i][0] - b[i][0]) <= EPS


# def test_solve_slae_3():
# a = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
# b = [[15], [-9], [5]]
# res = inv_m.solve_slae(a, b)
# assert mx.mul_matrix(a, res) == b


def test_solve_slae_4():
    a = [[4, 2, -1], [5, 3, -2], [3, 2, -3]]
    b = [[1], [2], [0]]
    res = mx.mul_matrix(a, inv_m.solve_slae(a, b))
    for i in range(len(res)):
        assert abs(res[i][0] - b[i][0]) <= EPS
