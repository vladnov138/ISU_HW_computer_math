import matrix.matrix as mx
import slae_by_inverse_matrix.slae_by_inverse_matrix as inv_m


def split_matrix(coords_matrix):
    """Return y values as result and replace y values to 1 in coords_matrix"""
    copy_coords_matrix = mx.get_copy(coords_matrix)
    res = []
    for i in range(len(copy_coords_matrix)):
        res.append([copy_coords_matrix[i][-1]])
        copy_coords_matrix[i][-1] = 1
    return res, copy_coords_matrix


def get_line_equation(coords_matrix):
    """Return line equation"""
    res, new_coords_matrix = split_matrix(coords_matrix)
    equation_matrix = inv_m.solve_slae(new_coords_matrix, res)
    return equation_matrix


def interpolate(coords_matrix):
    """Return interpolate value"""
    equation_matrix = get_line_equation(coords_matrix)
    x = min(coords_matrix[1][0], coords_matrix[0][0]) + \
        (max(coords_matrix[1][0], coords_matrix[0][0]) - min(coords_matrix[1][0], coords_matrix[0][0])) / 2
    return [[x], [x * equation_matrix[0][0] + equation_matrix[-1][-1]]]


def extrapolate(coords_matrix, indent=3):
    """Return extrapolate value"""
    equation_matrix = get_line_equation(coords_matrix)
    x = min(coords_matrix[1][0], coords_matrix[0][0]) - indent
    return [[x], [x * equation_matrix[0][0] + equation_matrix[-1][-1]]]


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


def get_lagranzh_polinomial(data_xy, x):
    """Return lagranzh polinomial value"""
    s = 0
    for i in range(len(data_xy)):
        s += data_xy[i][1] * get_product(data_xy, i, x)
    return s


def get_product(data_xy, i, x):
    """Return a product of range"""
    prod = 1
    for j in range(len(data_xy)):
        if j != i:
            prod *= (x - data_xy[j][0]) / (data_xy[i][0] - data_xy[j][0])
    return prod
