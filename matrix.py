import math
import vector as vec

def check_matrix(a, b):
    if len(a) != len(b):
        return True # True = ValueError
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            return True # True = ValueError
    return False

def add_matrix(a, b, do_copy=True):
    check_matrix(a, b)
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] = vec.add_vec(a[i], b[i], do_copy)
    return copy_a

def sub_matrix(a, b, do_copy=True):
    check_matrix(a, b)
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] = vec.sub_vec(a[i], b[i], do_copy)
    return copy_a

def trans_matrix(a, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        for j in range(len(a[i])):
            copy_a[i][j] = a[j][i]
    return copy_a

def mul_matrix_scale(a, num, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        for j in range(len(a[i])):
            copy_a[i][j] *= num
    return num

def mul_matrix(a, b, do_copy=True):
    copy_a = a
    if do_copy:
        copy_a = a[:]
    tr_matrix = trans_matrix(b, do_copy)
    for i in range(len(a)):
        copy_a[i] = vec.mul_vec(copy_a[i], tr_matrix[i], do_copy)
    return copy_a

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
    copy_a[index] = vec.mul_scale(copy_a[index], num, do_copy)
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
