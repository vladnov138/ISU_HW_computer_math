import modules.matrix.matrix as mx


def sort_rows(a):
    """Return a result of sorting matrix row by main diagonal"""
    for i in range(len(a[0])):
        index_a = -1
        for j in range(i, len(a)):
            if a[j][i] == 0:
                index_a = j
            elif index_a != -1:
                mx.change_row(a, index_a, j, do_copy=False)
    # print('r', a)


def solve_slae(*matrices, reversed=False):
    """Return a result of solving a system of linear algebraic equations"""
    a = matrices[0]
    if len(matrices) != 2 and not reversed:
        raise ValueError(f"Expected two matrices, but {len(matrices)} were given")
    if len(matrices) != 1 and reversed:
        raise ValueError(f"Expected one matrix, but {len(matrices)} were given")
    if len(matrices) == 2:
        b = matrices[1]
        mx.is_square(mx.trans_matrix(a))
        for row in b:
            a = mx.trans_matrix(mx.create_new_row(mx.trans_matrix(a), row))
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
