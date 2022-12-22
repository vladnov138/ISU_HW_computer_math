from math import acos

from matplotlib import pyplot as plt

from num_series_pkg.num_series import *


def show_graphic(func, x_max, n, check_func, indent=1):
    series_y_list = []
    y_list = []
    x_list = [i / 100 for i in range(-x_max * 100, x_max * 100 + 1)]
    for x in x_list:
        series_y_list.append(expand(x, n, func=func))
    plt.plot(x_list, series_y_list)
    plt.title(func.__name__)
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    for x in x_list:
        y_list.append(check_func(x))
    plt.plot(x_list, y_list)
    plt.axis([min(x_list) - indent, max(x_list) + indent,
              min(series_y_list) - indent, max(series_y_list) + indent])
    plt.show()


show_graphic(expand_arccos, 1, 1, check_func=acos)
