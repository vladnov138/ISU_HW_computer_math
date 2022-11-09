import modules.matrix.matrix as mx
import modules.slae_by_gauss.slae_by_gauss as gauss


def solve_slae(a, b):
    """Return new matrix by solving SLAE by inverse matrix"""
    return mx.mul_matrix(get_inverse_matrix(a), b)


def get_inverse_matrix(a):
    """Return new matrix by inversing the matrix"""
    mx.is_square(a)
    identity = mx.get_identity_matrix(len(a))
    result = gauss.solve_slae(a, identity)
    for i in range(len(result)):
        result[i] = result[i][-len(result[i]) // 2:]
    return result
