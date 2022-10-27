from matrix import matrix as mx


def sort_rows(a):
    """Return a result of sorting matrix row by main diagonal"""
    for i in range(len(a[0])):
        index_a = -1
        for j in range(i, len(a)):
            if a[j][i] == 0:
                index_a = j
            elif index_a != -1:
                mx.change_row(a, index_a, j, do_copy=False)


def solve_slae(a, do_copy=True, reversed=False):
    """Return a result of solving a system of linear algebraic equations"""
    mx.is_square(mx.trans_matrix(a)[:-1])
    c = mx.get_copy(a, do_copy)
    for i in range(0, len(a)):
        mx.mul_matrix_row_scale(c, 1 / c[i][i], i, do_copy=False)
        for j in range(i + 1, len(a)):
            b = mx.mul_matrix_row_scale(c, c[j][i], i)
            mx.sub_matrix_row(c, b, j, i, do_copy=False)
        sort_rows(c)
    if not reversed:
        return solve_slae(reverse(c), do_copy, True)
    return [mx.trans_matrix(c)[-1][::-1]]  # reverse the matrix back


def reverse(a):
    """Reverse matrix row and column and return a new matrix"""
    a = a[::-1]
    for i in range(len(a) // 2):
        a = mx.change_column(a, i, len(a) - i - 1, do_copy=False)
    return a
