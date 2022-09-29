import vector as vec


def check_matrix(a, b):
    if len(a) != len(b):
        return True  # True = ValueError
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            return True  # True = ValueError
    return False


def matrix_getlen(a):
    return len(a), len(a[0])


def add_matrix(a, b, do_copy=True):
    if check_matrix(a, b):
        raise ValueError("Некорректная размерность матриц")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] = vec.add_vec(a[i], b[i], do_copy)
    return copy_a


def sub_matrix(a, b, do_copy=True):
    if check_matrix(a, b):
        raise ValueError("Некорректная размерность матриц")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] = vec.sub_vec(a[i], b[i], do_copy)
    return copy_a


def trans_matrix(a):
    n, m = matrix_getlen(a)
    new_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][i] = a[i][j]
    return new_matrix


def mul_matrix_scale(a, num, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        for j in range(len(a[i])):
            copy_a[i][j] *= num
    return copy_a


def mul_matrix(a, b):
    n_a, m_a = matrix_getlen(a)
    n_b, m_b = matrix_getlen(b)
    if m_a != n_b:
        raise ValueError("Некорректная размерность матрицы для умножения!")
    new_matrix = [[0 for _ in range(n_a)] for _ in range(m_a)]
    tr_matrix = trans_matrix(b)
    for i in range(len(a)):
        for j in range(len(a[i])):
            new_matrix[i][j] = vec.mul_vec(a[i], tr_matrix[j])
    return new_matrix


def get_row(a, index):
    return a[index]


def get_col(a, index):
    return get_row(trans_matrix(a), index)


def change_row(a, start_index, new_index, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    t = copy_a[start_index]
    copy_a[start_index] = copy_a[new_index]
    copy_a[new_index] = t
    return copy_a


def mul_matrix_row_scale(a, num, index, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    copy_a[index] = vec.mul_scale(copy_a[index], num, do_copy)[:]
    return copy_a


def add_matrix_row(a, b, index_a, index_b, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    return vec.add_vec(copy_a[index_a], b[index_b], False)


def sub_matrix_row(a, b, index_a, index_b, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    return vec.sub_vec(copy_a[index_a], b[index_b], True)
