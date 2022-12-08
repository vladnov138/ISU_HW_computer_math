from matplotlib import pyplot as plt

from approximation_pkg.approximation import *
from interpolation_pkg.interpolation_view import get_x, get_y


def show_apprx(data_xy, points_x=0, power=1, func='', indent=1):
    """Draw approximation by pyplot"""
    points_data_x = get_x(data_xy)
    points_data_y = get_y(data_xy)
    # Generate x values
    x = [[i / 10 for i in range((min(get_x(data_xy)) - indent) * 10,
                                (max(get_y(data_xy)) + indent) * 10 + 1)]]
    y = apprx(data_xy, x, power=power, func=func)
    plt.plot(x[0], mx.trans_matrix(y)[0], color="blue")
    # Points from data_xy
    plt.scatter(points_data_x, points_data_y, color="blue")
    # Points from points_x (function argument)
    points_y = apprx(data_xy, points_x, power=power, func=func)
    plt.scatter(points_x, points_y, color="orange")
    plt.axis([min(get_x(data_xy)) - indent, max(get_x(data_xy)) + indent,
              min(get_y(data_xy)) - indent, max(get_y(data_xy)) + indent])
    plt.title("Approximation")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    plt.show()


def gh(x):
    return [x, 1]


data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
x = [[1, 3, 5]]
show_apprx(data_xy, points_x=x, func=gh, indent=10)
