import vector as vec


def check_matrix(a, b):
    if len(a) != len(b) or check_cols_len(a) or check_cols_len(b):
        return True  # True = ValueError
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            return True  # True = ValueError
    return False


def check_cols_len(a):
    len_value = len(a[0])
    for i in range(1, len(a)):
        if len_value != len(a[i]):
            return True  # True = ValueError
    return False


def is_square(a):
    for i in a:
        if len(i) != len(a):
            return False  # True = ValueError
    return True


def matrix_get_len(a):
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
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матрицы")
    n, m = matrix_get_len(a)
    new_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][i] = a[i][j]
    return new_matrix


def mul_matrix_scale(a, num, do_copy=True):
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матрицы")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        for j in range(len(a[i])):
            copy_a[i][j] *= num
    return copy_a


def mul_matrix(a, b):
    if check_cols_len(a) or check_cols_len(b):
        raise ValueError("Некорректная размерность матриц")
    n_a, m_a = matrix_get_len(a)
    n_b, m_b = matrix_get_len(b)
    if m_a != n_b:
        raise ValueError("Некорректная размерность матрицы для умножения!")
    new_matrix = [[0 for _ in range(n_a)] for _ in range(m_a)]
    tr_matrix = trans_matrix(b)
    for i in range(len(a)):
        for j in range(len(a[i])):
            new_matrix[i][j] = vec.mul_vec(a[i], tr_matrix[j])
    return new_matrix


def get_row(a, index):
    if len(a) <= index or index < 0:
        raise ValueError("Индекс не соответствует размерам матрицы")
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матрицы")
    return a[index]


def get_col(a, index):
    if len(a[0]) <= index or index < 0:
        raise ValueError("Индекс не соответствует размерам матрицы")
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матрицы")
    return get_row(trans_matrix(a), index)


def change_row(a, start_index, new_index, do_copy=True):
    if len(a) <= start_index or len(a) <= new_index or start_index < 0 or new_index < 0:
        raise ValueError("Индексы не соответствуют размерам матрицы")
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матрицы")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    t = copy_a[start_index]
    copy_a[start_index] = copy_a[new_index]
    copy_a[new_index] = t
    return copy_a


def mul_matrix_row_scale(a, num, index, do_copy=True):
    if len(a) <= index or index < 0:
        raise ValueError("Индекс не соответствует размерам матрицы")
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матрицы")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    copy_a[index] = vec.mul_scale(copy_a[index], num, do_copy)[:]
    return copy_a


def add_matrix_row(a, b, index_a, index_b, do_copy=True):
    if len(a) <= index_a or len(b) <= index_b or index_b < 0 or index_a < 0:
        raise ValueError("Индексы не соответствуют размерам матрицы")
    if check_cols_len(a) or check_cols_len(b) or len(a[index_a]) != len(b[index_b]):
        raise ValueError("Некорректная размерность матриц")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    copy_a[index_a] = vec.add_vec(copy_a[index_a], b[index_b], do_copy)
    return copy_a


def sub_matrix_row(a, b, index_a, index_b, do_copy=True):
    if len(a) <= index_a or len(b) <= index_b or index_b < 0 or index_a < 0:
        raise ValueError("Индексы не соответствуют размерам матрицы")
    if check_cols_len(a) or check_cols_len(b) or len(a[index_a]) != len(b[index_b]):
        raise ValueError("Некорректная размерность матриц")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    copy_a[index_a] = vec.sub_vec(copy_a[index_a], b[index_b], do_copy)
    return copy_a


def create_new_row(a, new_row, do_copy=True):
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матриц")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    copy_a.append(new_row)
    return copy_a


def del_row(a, index, do_copy=True):
    if len(a) <= index or index < 0:
        raise ValueError("Индекс не соответствует размерам матрицы")
    if check_cols_len(a):
        raise ValueError("Некорректная размерность матриц")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    del copy_a[index]
    return copy_a


def count_determinant(a):
    if not is_square(a):
        raise ValueError("Матрица не является квадратной")
    l = [[0 for j in range(len(a))] for i in range(len(a))]
    u = l[:]
    det = 1
    for i in range(len(a)):
        for j in range(len(a)):
            c = 0
            if i <= j:
                for k in range(i + 1):
                    c += l[i][k] * u[k][j]
                u[i][j] = a[i][j] - c
            else:
                for k in range(i + 1):
                    c += l[i][k] * u[k][j]
                l[i][j] = (a[i][j] - c) / u[j][j]
            if i == j:
                det *= l[i][j]
    return det
