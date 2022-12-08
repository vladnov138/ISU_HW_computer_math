import interpolation_pkg.interpolation as intp
import matrix.matrix as mx
import slae_by_inverse_matrix.slae_by_inverse_matrix as inv_m


def lsm(a, b):
    """Returns an equation matrix by the least square method"""
    b_wave = mx.mul_matrix(mx.trans_matrix(a), b)
    a_wave = mx.mul_matrix(mx.trans_matrix(a), a)
    result = inv_m.solve_slae(a_wave, b_wave)
    return result


def apprx(data_xy, x_wave, power=1, func=''):
    """Returns a Y matrix by approximation"""
    data_xy = add_func(data_xy, func)
    x_wave = mx.trans_matrix(x_wave)
    data_xy = ap_power(data_xy, power)
    b, a = intp.split_matrix(data_xy)
    equation = lsm(a, b)
    x = mx.hstack(x_wave, [[1] * len(x_wave)])
    x = add_func(x, func)
    x = ap_power(x, power)
    y = mx.mul_matrix(x, equation)
    return y


def ap_power(data_xy, power):
    """Returns a new matrix by raising x position in power and swapping it"""
    for i in range(2, power + 1):
        line = [[x ** i for x in mx.trans_matrix(data_xy)[-2]]]
        data_xy = mx.hstack(data_xy, line)
        for j in range(len(data_xy[0]) - 1, 0, -1):
            data_xy = mx.change_column(data_xy, j, j - 1)
    return data_xy


def add_func(data_xy, func):
    """Returns a new matrix by adding a new column with function value"""
    if type(func).__name__ == 'str':
        return data_xy
    # import math
    # if type(func).__name__ != type(math.cos).__name__:
    #     raise ValueError("Invalid type of function")
    line = [[func(x) for x in mx.trans_matrix(data_xy)[0]]]
    data_xy = mx.hstack(data_xy, line)
    for i in range(len(data_xy[0]) - 1, 0, -1):
        data_xy = mx.change_column(data_xy, i, i - 1)
    return data_xy
