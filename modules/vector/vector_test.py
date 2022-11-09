import vector as vec


def test_add_vectors():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [5, 10, 6]
    assert exp == vec.add_vec(a, b)


def test_sub_vectors():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [-3, -6, 4]
    assert exp == vec.sub_vec(a, b)


def test_mul_vec():
    a = [1, 2, -5, 2]
    b = [4, 8, 1, -2]
    ans = 11
    assert ans == vec.mul_vec(a, b)


def test_get_angle():
    a = [3, 4]
    b = [4, 3]
    ans = 16.26
    assert int(ans * 100) == int(vec.get_angle(a, b) * 100)


def test_proj_scale():
    a = [1, 2]
    b = [3, 4]
    ans = 2.2
    assert ans == vec.proj_scale(a, b)


def test_proj_vec():
    a = [4, 5]
    b = [6, 0]
    ans = [4, 0]
    assert ans == vec.proj_vec(a, b)


def test_mul_scale():
    a = [2, 5]
    num = 5
    ans = [10, 25]
    assert ans == vec.mul_scale(a, num)


def test_div_scale():
    a = [8, 16]
    num = 8
    ans = [1, 2]
    assert ans == vec.div_scale(a, num)


def test_is_collinear():
    a = [2, 6, -3]
    b = [6, 18, -9]
    ans = True
    assert ans == vec.is_collinear(a, b)


def test_dir():
    a = [2, 6, -3]
    b = [6, 18, -9]
    ans = True
    assert ans == vec.is_vec_dir(a, b)


def test_undir():
    a = [2, 6, -3]
    b = [6, 18, -9]
    ans = False
    assert ans == vec.is_vec_undir(a, b)


def test_normal_vec():
    a = [-3, -4]
    ans = [-0.6, -0.8]
    assert ans == vec.normal_vec(a)


def test_cos_vecs():
    a = [3, 4]
    b = [4, 3]
    ans = 0.96
    assert ans == vec.cos_vecs(a, b)
