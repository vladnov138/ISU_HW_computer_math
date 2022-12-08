from matplotlib import pyplot as plt

from interpolation_pkg.interpolation import interpolate, interpolate_piece_line, extrapolate, get_lagrange_polinomial
from matrix import matrix as mx


def show_interpolate(points_array, indent=1):
    """Draw interpolation line"""
    copy_points_array = mx.get_copy(points_array)
    x = get_x(points_array)
    y = get_y(points_array)
    plt.scatter(x, y, color='blue')
    intr_point = interpolate(points_array)
    extr_point = extrapolate(points_array, indent=indent)
    plt.scatter(intr_point[0], intr_point[1], color="orange")
    plt.scatter(extr_point[0], extr_point[1], color="orange")
    copy_points_array = sorted(mx.stack(mx.stack(mx.trans_matrix(intr_point), mx.trans_matrix(extr_point)),
                                        copy_points_array))
    x = get_x(copy_points_array)
    y = get_y(copy_points_array)
    plt.title("Line interpolation")
    generate_plot(x, y)


def generate_plot(x, y):
    """Show plot"""
    plt.plot(x, y)
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    plt.show()


def show_interpolate_piece_line(data_xy):
    """Draw piece line interpolation by pyplot"""
    copy_data_xy = mx.get_copy(data_xy)
    x = get_x(data_xy)
    y = get_y(data_xy)
    plt.scatter(x, y, color="blue")
    points = interpolate_piece_line(data_xy)
    intr_points = points[1:-1]
    extr_points = [points[0], points[-1]]
    plt.scatter(mx.trans_matrix(intr_points)[0], mx.trans_matrix(intr_points)[1], color="orange")
    plt.scatter(mx.trans_matrix(extr_points)[0], mx.trans_matrix(extr_points)[1], color="orange")
    copy_data_xy = sorted(mx.stack(copy_data_xy, mx.stack(intr_points, extr_points)))
    x = get_x(copy_data_xy)
    y = get_y(copy_data_xy)
    plt.title("Piece line interpolation")
    generate_plot(x, y)


def get_x(data_xy):
    """Returns x array from data_xy"""
    return mx.trans_matrix(data_xy)[0][:]


def get_y(data_xy):
    """Returns y array from data_xy"""
    return mx.trans_matrix(data_xy)[1][:]


def show_lagrange(data_xy, indent=1):
    """Draw Lagrange polinomial by pyplot"""
    data_x = mx.trans_matrix(data_xy)[0][:]
    x = get_x(data_xy)
    y = get_y(data_xy)
    plt.scatter(x, y, color="blue")
    plt.axis([min(x) - 1, max(x) + indent, min(y) - indent, max(y) + indent])
    x = [i / 10 for i in range((min(data_x) - indent) * 10, (max(data_x) + indent) * 10 + 1)]
    y = [get_lagrange_polinomial(data_xy, x[i]) for i in range(len(x))]
    plt.title("Lagranzh polinomial")
    generate_plot(x, y)


data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
coords_matrix = [[2, 5], [6, 9]]
# show_lagranzh(data_xy)
