from interpolation_pkg.interpolation import *

EPS = 1e-10


def test_split_matrix():
    coords_matrix = [[2, 5], [6, 9]]
    ans_coords_matrix = [[2, 1], [6, 1]]
    ans = [[5], [9]]
    res, new_matrix = split_matrix(coords_matrix)
    assert ans == res
    assert new_matrix == ans_coords_matrix


def test_get_line_equation():
    coords_matrix = [[2, 5], [6, 9]]
    ans = [[1], [3]]
    assert ans == get_line_equation(coords_matrix)


def test_interpolate():
    coords_matrix = [[2, 5], [6, 9]]
    ans = [[4], [7]]
    assert ans == interpolate(coords_matrix)


def test_extrapolate():
    coords_matrix = [[2, 5], [6, 9]]
    ans = [[1], [4]]
    assert ans == extrapolate(coords_matrix, indent=1)


def test_interpolate_piece_line():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    ans = [[-2, -1], [2, 3], [3.25, 3.5], [4.75, 5], [6.5, 7.8]]
    res = interpolate_piece_line(data_xy)
    assert mx.equal_matrix_eps(ans, res, EPS)


def test_get_lagrange_polinomial():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    for i in range(len(data_xy)):
        assert get_lagrange_polinomial(data_xy, data_xy[i][0]) == data_xy[i][1]


def test_get_product():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    i = 0
    x = data_xy[0][0]
    assert x == get_product(data_xy, i, x)
