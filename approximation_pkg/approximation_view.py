from matplotlib import pyplot as plt

from approximation_pkg.approximation import *
from interpolation_pkg.interpolation_view import get_x, get_y


def show_apprx(data_xy, x_wave, power=1, indent=1):
    """Draw approximation by pyplot"""
    points_data_x = get_x(data_xy)
    points_data_y = get_y(data_xy)
    # Generate x values
    x = [[i / 10, 1] for i in range((min(get_x(data_xy)) - indent) * 10,
                                    (max(get_y(data_xy)) + indent) * 10 + 1)]
    y = apprx(data_xy, x, power=power)
    plt.plot(get_x(x), get_y(y), color="blue")
    # Points from data_xy
    plt.scatter(points_data_x, points_data_y, color="blue")
    # Points from x_wave
    points_y = apprx(data_xy, x_wave, power=power)
    plt.scatter(get_x(x_wave), points_y, color="orange")
    plt.axis([min(get_x(data_xy)) - indent, max(get_x(data_xy)) + indent,
              min(get_y(data_xy)) - indent, max(get_y(data_xy)) + indent])
    plt.title("Approximation")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    plt.show()


data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
x = [[1, 1], [3, 1], [5, 1]]
show_apprx(data_xy, x, power=1, indent=10)
