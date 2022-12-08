import math


def check_vecs(a, b):
    """Return a ValueError if vectors lengths are different"""
    check_len_vec(a)
    check_len_vec(b)
    if len(a) != len(b):
        raise ValueError("The vectors lengths are different!")


def check_len_vec(a):
    """Return a ValueError if vectors lengths are invalid"""
    if len(a) < 1:
        raise ValueError("Invalid vector length")


def get_copy(a, do_copy):
    """Return a copy of vector if do_copy is true"""
    if do_copy:
        return a[:]
    return a


def add_vec(a, b, do_copy=True):
    """Return a new vector by sum"""
    check_vecs(a, b)
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        a[i] += b[i]
    return a


def sub_vec(a, b, do_copy=True):
    """Return a new vector by subtracting"""
    b = get_copy(b, do_copy)
    for i in range(len(b)):
        b[i] *= -1
    return add_vec(a, b)


def mul_vec(a, b):
    """Return a new vector by multiplying"""
    check_vecs(a, b)
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def mul_scale(a, num, do_copy=True):
    """Return a new vector by multiplying by a scalar"""
    check_len_vec(a)
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        a[i] *= num
    return a


def div_scale(a, num, do_copy=True):
    """Return a new vector by dividing by a scalar"""
    check_len_vec(a)
    if num == 0:
        raise ValueError("Invalid value of scalar!")
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        a[i] /= num
    return a


def is_collinear(a, b):
    """Return if vector are collinear"""
    check_vecs(a, b)
    return abs(cos_vecs(a, b)) == 1


def is_vec_dir(a, b):
    """Return if vectors are co-directions"""
    check_vecs(a, b)
    return cos_vecs(a, b) == 1


def is_vec_undir(a, b):
    """Return if vectors have opposite directions"""
    check_vecs(a, b)
    return cos_vecs(a, b) == -1


def get_len(a):
    """Return a vector length"""
    check_len_vec(a)
    result = 0
    for i in range(len(a)):
        result += a[i] ** 2
    return result ** 0.5


def equal_vecs(a, b):
    """Return if vectors are equal"""
    check_vecs(a, b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def equal_vecs_eps(a, b, eps):
    """Return if vectors are equal by eps"""
    check_vecs(a, b)
    for i in range(len(a)):
        if abs(a[i] - b[i]) >= eps:
            return False
    return True


def is_orthogonal(a, b):
    """Return if orthogonal vectors"""
    check_vecs(a, b)
    return cos_vecs(a, b) == 0


def normal_vec(a, do_copy=True):
    """Return a new normalize vector"""
    check_len_vec(a)
    a = get_copy(a, do_copy)
    length = get_len(a)
    for i in range(len(a)):
        a[i] /= length
    return a


def change_dir(a, do_copy=True):
    """Return a new vector with opposite direction"""
    check_len_vec(a)
    a = get_copy(a, do_copy)
    for i in range(len(a)):
        a[i] *= -1
    return a


def cos_vecs(a, b):
    """Return a cos between two vectors"""
    check_vecs(a, b)
    return mul_vec(a, b) / (get_len(a) * get_len(b))


def get_angle(a, b, degrees=True):
    """Return an angle in degrees between two vectors"""
    check_vecs(a, b)
    if degrees:
        return math.acos(cos_vecs(a, b)) * 180 / math.pi  # Transform to degrees
    else:
        return math.acos(cos_vecs(a, b))


def proj_vec(a, b):
    """Return a projection vector"""
    check_vecs(a, b)
    return mul_scale(b, proj_scale(a, b) / get_len(b))


def proj_scale(a, b):
    """Return a projection scalar"""
    check_vecs(a, b)
    return mul_vec(a, b) / get_len(b)
