import copy

import modules.vector.vector as vec


def check_matrix(a, b):
    """Return a ValueError if the matrices lengths are different or matrices columns lengths
    are different"""
    if len(a) != len(b):
        raise ValueError("The matrices lengths are different!")
    check_row_lens(a)
    check_row_lens(b)
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            raise ValueError("The matrices columns length are different!")


def check_row_lens(a):
    """Return a ValueError if the matrix rows lengths are different"""
    len_value = len(a[0])
    for i in range(1, len(a)):
        if len_value != len(a[i]):
            raise ValueError(f"The matrix rows lengths are different: {a}")


def check_index(a, index):
    """Return a ValueError if the index is invalid"""
    if len(a) <= index or index < 0:
        raise ValueError("Index is invalid")
    check_row_lens(a)


def check_rows(a, b, index_a, index_b):
    """Return a ValueError if matrices rows lengths are different"""
    check_index(a, index_a)
    check_index(b, index_b)
    if len(a[index_a]) != len(b[index_b]):
        raise ValueError("Row lengths are different!")


def get_copy(a, do_copy):
    """Return a copy of matrix if do_copy is true"""
    if do_copy:
        return copy.deepcopy(a)
    return a


def is_square(a):
    """Return a ValueError if the matrix isn't square"""
    for i in a:
        if len(i) != len(a):
            raise ValueError(f"The matrix isn't square: {a}")


def matrix_get_len(a):
    """Return a matrix column length and a matrix row length"""
    return len(a), len(a[0])


def add_matrix(a, b, do_copy=True):
    """Return a new matrix by sum two matrices"""
    check_matrix(a, b)
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        a[i] = vec.add_vec(a[i], b[i], do_copy)
    return a


def sub_matrix(a, b, do_copy=True):
    """Return a new matrix by subtracting two matrices"""
    check_matrix(a, b)
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        a[i] = vec.sub_vec(a[i], b[i], do_copy)
    return a


def trans_matrix(a):
    """Return a new matrix by transposing the matrix"""
    check_row_lens(a)
    n, m = matrix_get_len(a)
    new_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][i] = a[i][j]
    return new_matrix


def mul_matrix_scale(a, num, do_copy=True):
    """Return a new matrix by multiplying the matrix and the scalar"""
    check_row_lens(a)
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= num
    return a


def mul_matrix(a, b):
    """Return a new matrix by multiplying two matrices"""
    check_row_lens(a)
    check_row_lens(b)
    n_a, m_a = matrix_get_len(a)
    n_b, m_b = matrix_get_len(b)
    if m_a != n_b:
        raise ValueError("Invalid matrices lengths for multiplying!")
    new_matrix = [[0 for _ in range(m_b)] for _ in range(n_a)]
    tr_matrix = trans_matrix(b)
    for i in range(len(a)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = vec.mul_vec(a[i], tr_matrix[j])
    return new_matrix


def get_row(a, index, do_copy=True):
    """Return a row by index"""
    check_index(a, index)
    vec.get_copy(a[index], do_copy)
    return a[index]


def get_col(a, index):
    """Return a column by index"""
    check_index(a, index)
    return get_row(trans_matrix(a), index)


def change_row(a, start_index, new_index, do_copy=True):
    """Swap two rows by their indexes and return a new matrix"""
    check_index(a, start_index)
    check_index(a, new_index)
    a = get_copy(a, do_copy)
    t = a[start_index]
    a[start_index] = a[new_index]
    a[new_index] = t
    return a


def change_column(a, start_index, new_index, do_copy=True):
    """Swap two columns by their indexes and return a new matrix"""
    check_index(a, start_index)
    check_index(a, new_index)
    a = get_copy(a, do_copy)
    a = trans_matrix(change_row(trans_matrix(a), start_index, new_index, do_copy=False))
    return a


def mul_matrix_row_scale(a, num, index, do_copy=True):
    """Multiply matrix row by index and return the new matrix with result row"""
    check_index(a, index)
    a = get_copy(a, do_copy)
    a[index] = vec.mul_scale(a[index], num, do_copy)[:]
    return a


def add_matrix_row(a, b, index_a, index_b, do_copy=True):
    """Summarize matrices rows by their indexes and return the new matrix with result row"""
    check_rows(a, b, index_a, index_b)
    a = get_copy(a, do_copy)
    a[index_a] = vec.add_vec(a[index_a], b[index_b], do_copy)
    return a


def sub_matrix_row(a, b, index_a, index_b, do_copy=True):
    """Subtract matrices rows by their indexes and returns the new matrix with result row"""
    check_rows(a, b, index_a, index_b)
    a = get_copy(a, do_copy)
    a[index_a] = vec.sub_vec(a[index_a], b[index_b], do_copy)
    return a


def create_new_row(a, new_row, do_copy=True):
    """Create new row to the matrix and return the new matrix with new row"""
    check_row_lens(a)
    if len(a[0]) != len(new_row):
        raise ValueError("Row lengths are different!")
    a = get_copy(a, do_copy)
    a.append(new_row)
    return a


def del_row(a, index, do_copy=True):
    """Delete the matrix row by index and return the new matrix without this row"""
    check_index(a, index)
    a = get_copy(a, do_copy)
    del a[index]
    return a


def count_determinant(a):
    """Return a matrix determinant by LU decomposition"""
    is_square(a)
    l = [[0 for j in range(len(a))] for i in range(len(a))]  # lower part of matrix
    u = copy.deepcopy(l)  # upper part of matrix
    for i in range(len(l)):
        l[i][i] = 1

    det = 1
    for i in range(len(a)):
        for j in range(len(a)):
            s = 0  # sum
            if i <= j:
                for k in range(i + 1):
                    s += l[i][k] * u[k][j]
                u[i][j] = a[i][j] - s
                print(a[i][j], s)
            else:
                for k in range(j + 1):
                    s += l[i][k] * u[k][j]
                if u[j][j] != 0:
                    l[i][j] = (a[i][j] - s) / u[j][j]
            if i == j:
                det *= u[i][j]
    return det


def hstack(a, b):
    """Return united matrix"""
    for row in b:
        a = trans_matrix(create_new_row(trans_matrix(a), row))
    return a


def get_identity_matrix(size):
    """Return identity matrix"""
    identity = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        identity[i][i] = 1
    return identity
