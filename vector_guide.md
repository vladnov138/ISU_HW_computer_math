# vectors

These functions are created to perfom mathematical operations with vector
---
check_vecs(a, b) - this function checks that two vectors length are equals.
* a - the first vector (list).
* b - the second vector (list).
<br><br>It is boolean function which returns True if these vectors length are different and returns False if these vectors length are equals.
---
check_vec(a) - this function checks vector length.
* a - the vector (list)
<br><br>It is boolean function which returns True if vector length less 2 and return False if vector length is correct.
---
add_vec(a, b, do_copy=True) - this function summarizes two vectors.
* a - the first vector (list)
* b - the second vector (list)
* do_copy - boolean argument, if it is true, function won't change vectors a and b, else it will change vector a.
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>This function returns new vector - sum of two vectors.
---
sub_vec(a, b, do_copy=True) - this function subtracts two vectors.
* a - the first vector (list)
* b - the second vector (list)
* do_copy - boolean argument, if it is true, function won't change vectors a and b, else it will change vector a.
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>This function returns new vector - substract of two vectors.
---
mul_vec(a, b) - this function multiplies two vectors.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>It returns number - sum of multiplication of vectors coordinates.
---
scale_mul(a, num, do_copy=True) - this function miltiplies a vector by a scalar.
* a - the vector (list)
* num - the scalar (number)
* do_copy - boolean argument, if it is true, function won't change vectors a and b, else it will change vector a.
<br><br>If the vector length are less than 2, it'll return ValueError.
<br><br>It returns new vector - result of miltiplication the vector and the scalar.
---
div_scale(a, num, do_copy=True) - this function divides a vector by a scalar.
* a - the vector (list)
* num - the scalar
* do_copy - boolean argument, if it is true, function won't change vectors a and b, else it will change vector a.
<br><br>If the vector length are less than 2, it'll return ValueError.
<br><br>It returns new vector - result of division the vector by the scalar.
---
is_collinear(a, b) - this function checks vectors collinearity.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>If vectors are collinearity, it will return true, else it will return false.
---
is_vec_dir(a, b) - this function checks vectors co-direction.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>If vectors are co-directed it will return true, else it will return false
---
is_vec_undir(a, b) - this function checks vectors oppositely direction.
* a - the first vector (list)
* b - the second vector (list)
<br><br> If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br> If vectors are oppositely directed it will return true, else it will return false
---
get_len(a) - this function get a vector length.
* a - the vector (list)
<br><br>If the vector length less than 2, it will return ValueError.
<br><br>It returns number - the vector length.
---
equal_vecs(a, b) - this function equals two vectors.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>If the vectors are equals, it'll return True, else it'll return False
---
equal_vecs_eps(a, b, eps) - this function equals of vectors by parameter
* a - the first vector (list)
* b - the second vector (list)
* eps - small number
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>If the vectors are equals by parameter eps, it'll return true, else it'll return false.
---
is_orthogonal(a, b) - this function check orthogonality of two vectors.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>If this vectors are orthogonality to each other, it'll return true, else it'll return false.
---
normal_vec(a, do_copy=True) - this function normalize a vector.
* a - the vector (list)
* do_copy - boolean argument, if it is true, function won't change vectors a and b and will make a copy, else it will change vector a.
<br><br>If the vector length less than 2, it'll return ValueError.
<br><br>It returns new normalize vector.
---
change_dir(a, do_copy=True) - this function changes a vector direction.
* a - the vector (list)
* do_copy - boolean argument, if it is true, function won't change vectors a and b and will make a copy, else it will change vector a.
<br><br>If the vector length less than 2, it'll return ValueError.
<br><br>It returns the opossitely directed vector.
---
cos_vecs(a, b) - this function counts a cos of angle between two vectors.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>It returns a number - cos of angle.
---
get_angle(a, b) - this function counts an angle between two vectors.
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>It returns a number - degrees angle
---
proj_vec(a, b) - this function counts a projection
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>It returns a new vector - projection
---
proj_scale(a, b) - this function counts a projection 
* a - the first vector (list)
* b - the second vector (list)
<br><br>If the vectors length are different or vectors length less than 2, it'll return ValueError.
<br><br>It returns a number - projection
