import matrix as mx


def test_mul_matrix_scale():
    a = [[1, 2], [3, 4]]
    num = 2
    ans = [[2, 4], [6, 8]]
    assert ans == mx.mul_matrix_scale(a, num)


def test_add_matrix():
    a = [[1, 2], [3, 4]]
    b = [[3, 4], [-1, 3]]
    ans = [[4, 6], [2, 7]]
    assert ans == mx.add_matrix(a, b)


def test_sub_matrix():
    a = [[6, 7], [-4, 3]]
    b = [[1, 3], [2, -5]]
    ans = [[5, 4], [-6, 8]]
    assert ans == mx.sub_matrix(a, b)


def test_mul_matrix():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    ans = [[19, 22], [43, 50]]
    assert ans == mx.mul_matrix(a, b)


def test_trans_matrix():
    a = [[2, 3, 5], [5, 7, 6]]
    ans = [[2, 5], [3, 7], [5, 6]]
    assert ans == mx.trans_matrix(a)


def test_get_row():
    a = [[1, 2], [3, 4], [5, 6]]
    index = 1
    ans = [3, 4]
    assert ans == mx.get_row(a, index)


def test_get_col():
    a = [[1, 2], [3, 4], [5, 6]]
    index = 0
    ans = [1, 3, 5]
    assert ans == mx.get_col(a, index)


def test_change_row():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start_index = 0
    new_index = 1
    ans = [[4, 5, 6], [1, 2, 3], [7, 8, 9]]
    assert ans == mx.change_row(a, start_index, new_index)


def test_mul_matrix_row_scale():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    num = 2
    index = 2
    ans = [[1, 2, 3], [4, 5, 6], [14, 16, 18]]
    assert ans == mx.mul_matrix_row_scale(a, num, index)


def test_create_new_row():
    a = [[1, 2, 3], [4, 5, 6]]
    new_row = [10, 20, 30]
    ans = [[1, 2, 3], [4, 5, 6], [10, 20, 30]]
    assert ans == mx.create_new_row(a, new_row)


def test_del_row():
    a = [[1, 2, 3], [4, 5, 6]]
    index = 1
    ans = [[1, 2, 3]]
    assert ans == mx.del_row(a, index)


def test_add_matrix_row():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[10, 20, 30], [40, 50, 60]]
    index_a = 0
    index_b = 1
    ans = [[41, 52, 63], [4, 5, 6]]
    assert ans == mx.add_matrix_row(a, b, index_a, index_b)


def test_sub_matrix_row():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[10, 20, 30], [40, 50, 60]]
    index_a = 1
    index_b = 0
    ans = [[1, 2, 3], [-6, -15, -24]]
    assert ans == mx.sub_matrix_row(a, b, index_a, index_b)


def test_count_determinant():
    a = [[5, 4, 3], [21, -2, 6], [5, 4, 0]]
    ans = 282
    assert ans == mx.count_determinant(a)


def test_get_copy():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[10, 20, 30], [40, 50, 60]]
    num = 50
    ans = a.copy()
    mx.add_matrix(a, b)
    mx.sub_matrix(a, b)
    mx.mul_matrix_scale(a, num)
    assert ans == a
