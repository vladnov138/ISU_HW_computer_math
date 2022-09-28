import math


def check_vecs(a, b, do_copy=True):
    return check_vec(a) or check_vec(b) or len(a) != len(b)  # True = error


def check_vec(a):
    return len(a) < 2  # True = error


def add_vec(a, b):
    if check_vecs(a, b): return "error"
    for i in range(len(a)):
        a[i] += b[i]
    return a


def sub_vec(a, b):
    for i in range(len(b)):
        b[i] *= -1
    return add_vec(a, b)


def mul_vec(a, b):  # Скалярное произведение векторов
    if check_vecs(a, b): return "error"
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def mul_scale(a, num):  # Произведение вектора на скаляр
    if check_vec(a): return "error"
    for i in range(len(a)):
        a[i] *= num
    return a


def div_scale(a, num):
    if check_vec(a) or num == 0: return "error"
    for i in range(len(a)):
        a[i] /= num
    return a


def collinear(a, b):
    if check_vecs(a, b): return "error"
    return abs(cos_vecs(a, b)) == 1


def vec_dir(a, b):
    if check_vecs(a, b): return "error"
    return cos_vecs(a, b) == 1


def vec_undir(a, b):
    if check_vecs(a, b): return "error"
    return cos_vecs(a, b) == -1


def getlen(a):
    if check_vec(a): return "error"
    result = 0
    for i in range(len(a)):
        result += a[i] ** 2
    return result ** 0.5


def equal_vecs(a, b):
    if check_vecs(a, b): return "error"
    c = sub_vec(a, b)
    for i in range(len(c)):
        if c[i] != 0:
            return False
    return True


def equal_vecs_eps(a, b, eps):
    if check_vecs(a, b): return "error"
    c = sub_vec(a, b)
    for i in range(len(c)):
        if abs(c[i]) >= eps:
            return False
    return True


def ortogonal(a, b):
    if check_vecs(a, b): return "error"
    return cos_vecs(a, b) == 0


def normal_vec(a):
    if check_vec(a): return "error"
    length = getlen(a)
    for i in range(len(a)):
        a[i] /= length
    return a


def change_dir(a):
    if check_vec(a): return "error"
    for i in range(len(a)):
        a[i] *= -1
    return a


def cos_vecs(a, b):
    if check_vecs(a, b): return "error"
    if getlen(a) != 0 and getlen(b) != 0:
        return mul_vec(a, b) / (getlen(a) * getlen(b))
    return "Error: length of the vectors is 0"


def getangle(a, b):
    if check_vecs(a, b): return "error"
    if getlen(a) != 0 and getlen(b) != 0:
        return math.acos(cos_vecs(a, b)) * 180 / math.pi


def proj_vec(a, b):
    if check_vecs(a, b): return "error"
    if getlen(b) != 0:
        return mul_scale(b, proj_scale(a, b) / getlen(b))
    return "Error"


def proj_scale(a, b):
    if check_vecs(a, b): return "error"
    if getlen(b) != 0:
        return mul_vec(a, b) / getlen(b)
    return "Error"
