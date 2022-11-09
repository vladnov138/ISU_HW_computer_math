import modules.matrix.matrix as mx


def sort_rows(a):
    """Return a result of sorting matrix row by main diagonal"""
    for i in range(len(a[0])):
        index_a = -1
        for j in range(i, len(a)):
            if a[i][i] != 0:
                break
            elif index_a == -1:
                index_a = j
            else:
                mx.change_row(a, index_a, j, do_copy=False)
                index_a = -1
                break
        if index_a != -1:
            raise ValueError("There is no solution")


def solve_slae(*matrices, reversed=False):
    """Return a result of solving a system of linear algebraic equations"""
    if len(matrices) == 0 or len(matrices) > 2:
        raise ValueError("Invalid number of arguments")
    a = matrices[0]
    if len(matrices) == 2:
        a = mx.hstack(a, matrices[1])
    sort_rows(a)
    for i in range(0, len(a)):
        mx.mul_matrix_row_scale(a, 1 / a[i][i], i, do_copy=False)
        for j in range(i + 1, len(a)):
            temp = mx.mul_matrix_row_scale(a, a[j][i], i)  # multiplied row
            mx.sub_matrix_row(a, temp, j, i, do_copy=False)
        sort_rows(a)  # sort by diagonal
    if not reversed:
        return solve_slae(reverse(a), reversed=True)
    return reverse(a)  # reverse the matrix back and return the last column


def reverse(a):
    """Reverse matrix row and column and return a new matrix"""
    a = a[::-1]
    for i in range(len(a) // 2):
        a = mx.change_column(a, i, len(a) - i - 1, do_copy=False)
    return a
