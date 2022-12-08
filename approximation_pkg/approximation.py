import interpolation_pkg.interpolation as intp
import matrix.matrix as mx
import slae_by_inverse_matrix.slae_by_inverse_matrix as inv_m


def lsm(a, b):
    """Returns an equation matrix by the least square method"""
    b_wave = mx.mul_matrix(mx.trans_matrix(a), b)
    a_wave = mx.mul_matrix(mx.trans_matrix(a), a)
    result = inv_m.solve_slae(a_wave, b_wave)
    return result


def make_func(x, power):
    """Returns func values"""
    func = [x, 1]
    for i in range(2, power + 1):
        val = x ** i
        func.insert(0, val)
    return func


def apprx(data_xy, x_wave, power=1, func=make_func):
    """Returns a Y matrix by approximation"""
    a = [func(row_xy[0], power) for row_xy in data_xy]
    x_wave = [func(x[0], power) for x in x_wave]
    b, _ = intp.split_matrix(data_xy)
    equation = lsm(a, b)
    y = mx.mul_matrix(x_wave, equation)
    return y
