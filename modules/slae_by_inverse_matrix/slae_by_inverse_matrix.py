import modules.matrix.matrix as mx
import modules.slae_by_gauss.slae_gauss as gauss


def solve_slae(a, b):
    """Return new matrix by solving SLAE by inverse matrix"""
    x = mx.mul_matrix(get_inverse_matrix(a), b)
    return x


def get_inverse_matrix(a):
    """Return new matrix by inversing the matrix"""
    if (mx.count_determinant(a) == 0):
        raise ValueError("The inverse matrix doesn't exist")
    identity = get_identity_matrix(len(a))
    result = gauss.solve_slae(a, identity)
    for i in range(len(result)):
        result[i] = result[i][-len(result[i]) // 2:]
    return result


def get_identity_matrix(size):
    """Return identity matrix"""
    identity = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        identity[i][i] = 1
    return identity
