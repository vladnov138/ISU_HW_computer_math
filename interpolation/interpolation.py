import math
import random
from matplotlib import pyplot as plt

import slae_by_inverse_matrix.slae_by_inverse_matrix as inv_m
import matrix.matrix as mx

def split_matrix(coords_matrix):
    """Return y values as result and replace y values to 1 in coords_matrix"""
    res = []
    for i in range(len(coords_matrix)):
        res.append([coords_matrix[i][-1]])
        coords_matrix[i][-1] = 1
    return res

def get_line_equation(coords_matrix):
    """Return line equation"""
    copy_coords_matrix = [elem[:] for elem in coords_matrix]
    res = split_matrix(copy_coords_matrix)
    equation_matrix = inv_m.solve_slae(copy_coords_matrix, res)
    return equation_matrix


def interpolate(coords_matrix):
    """Return interpolate value"""
    # print(coords_matrix)
    equation_matrix = get_line_equation(coords_matrix)
    x = min(coords_matrix[1][0], coords_matrix[0][0]) + \
        (max(coords_matrix[1][0], coords_matrix[0][0]) - min(coords_matrix[1][0], coords_matrix[0][0])) / 2
    return [[x], [x * equation_matrix[0][0] + equation_matrix[-1][-1]]]


def extrapolate(coords_matrix, indent=3):
    """Return extrapolate value"""
    equation_matrix = get_line_equation(coords_matrix)
    x = min(coords_matrix[1][0], coords_matrix[0][0]) - indent
    return [[x], [x + equation_matrix[-1][-1]]]


def interpolate_piece_line(data_xy, indent=3):
    """Return interpolate value of piece function"""
    xy_matrix = []
    for i in range(len(data_xy) - 1):
        copy_data_xy = [elem[:] for elem in data_xy]
        a = copy_data_xy[i:i + 2]
        if i == 0:
            xy_matrix.append(mx.trans_matrix(extrapolate(a, indent=indent))[0])
        xy_matrix.append(mx.trans_matrix(interpolate(a))[0])
        if i == len(data_xy) - 2:
            xy_matrix.append(mx.trans_matrix(extrapolate(a, indent=-indent))[0])
    return xy_matrix

def get_lagrange_polinomial(data_xy, x):
    """"""
    s = 0
    for i in range(len(data_xy)):
        s += data_xy[i][1] * get_product(data_xy, i, x)
    return s

def get_product(data_xy, i, x):
    """Return a product of range"""
    prod = 1
    for j in range(len(data_xy)):
        if j == i:
            continue
        prod *= (x - data_xy[j][0]) / (data_xy[i][0] - data_xy[j][0])
    return prod

def show_interpolate_extrapolate():
    x = [2, 6]
    y = [5, 9]
    plt.plot(x, y)
    intr_steps = interpolate([[2, 5], [6, 9]])
    plt.step(intr_steps[0], intr_steps[1], "b-o")
    extr_steps = extrapolate([[2, 5], [6, 9]], indent=1)
    plt.step(extr_steps[0], extr_steps[1], "g-o")
    plt.show()

def show_interpolate_piece_line():
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [1, 3, 3.5, 6]
    y = [2, 4, 3, 7]
    plt.plot(x, y)
    # ans = [[-2, -1], [2, 3], [3.25, 3.5], [4.75, 5], [6.5, 3.9]]
    steps = interpolate_piece_line(data_xy)
    intr_steps = steps[1:-1]
    plt.scatter(mx.trans_matrix(intr_steps)[0], mx.trans_matrix(intr_steps)[1], color="blue")
    extr_steps = [steps[0], steps[-1]]
    plt.scatter(mx.trans_matrix(extr_steps)[0], mx.trans_matrix(extr_steps)[1], color="orange")
    plt.show()

show_interpolate_piece_line()