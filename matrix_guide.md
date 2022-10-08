# Matrix

These functions are created to perfom mathematical operations with vector
---
check_matrix(a, b) - this function checks matrices length, rows length and columns length.
* a - the first matrix
* b - the second matrix
<br><br>It'll return true if the matrices length or rows length or columns length are different, else it'll return False.
---
check_cols_len(a) - this function checks columns length
* a - the matrix
<br><br>It'll return true if the matrix columns length are diffrent, else it'll return false
---
is_square(a) - this function checks if a matrix is square.
* a - the matrix
<br><br>It'll return true if the matrix is square, else it'll return false.
---
matrix_get_len(a) - this function gets a matrix length
* a - the matrix
<br><br>It returns two numbers - the matrix columns length and the matrix rows length.
---
add_matrix(a, b, do_copy=True) - this function summarizes two matrices.
* a - the first matrix
* b - the second matrix
* do_copy - boolean argument, if it is true, function won't change matrix a and b and make a copy, else it will change matrix a.
<br><br>If the matrices length are different, it'll return a ValueError
<br><br>It returns a new matrix - result of matrices sum
---
sub_matrix(a, b, do_copy=True) - this function substracts two matrices.
* a - the first matrix
* b - the second matrix
<br><br>If the matrices length are different, it'll return a ValueError
* do_copy - boolean argument, if it is true, function won't change matrix a and b and make a copy, else it will change matrix a.
<br><br>It returns a new matrix - result of matrices sub
---
trans_matrix(a) - this function transposes a matrix.
* a - the matrix
<br><br>If the matrix columns length are different, it'll return a ValueError.
<br><br>It returns a new matrix - a transposed matrix
---
mul_matrix_scale(a, num, do_copy=True) - this function multiplies a matrix by a scalar
* a - the matrix
* num - the scalar
* do_copy - boolean argument, if it is true, function won't change matrix a and make a copy, else it will change matrix a.
<br><br>If the matrix columns length are different, it'll return a ValueError.
<br><br>It returns a new matrix - a result of product.
---
mul_matrix(a, b) - this function multiplies a matrix by matrix
* a - the first matrix
* b - the second matrix
<br><br>If the matrix columns are different or matrices length are not suitable for multiplication, it'll return a ValueError
<br><br>It returns a new matrix - a result of product
---
get_row(a, index) - this function gets a row by an index
* a - the matrix
* index - the index of row
<br><br>If the matrix columns length are different or the matrix row length less than index or index less than 0, it'll return a ValueError
<br><br>It returns a vector - matrix row
---
get_col(a, index) - this function gets a column by an index
* a - the matrix
* index - the index of column
<br><br>If the matrix columns length are different or the matrix column length less than index or index less than 0, it'll return a ValueError
<br><br>It returns a vector - matrix column
---
change_row(a, start_index, new_index, do_copy=True) - this function changes rows by their indexes
* a - the matrix
* start_index - the initial index of matrix row
* new_index - the new index of matrix row
* do_copy - boolean argument, if it is true, function won't change matrix a and make a copy, else it will change matrix a.
<br><br>If the matrix columns length are different or the matrix row length less than initial index or less than new index, inital index or new index less than 0, 
it'll return a ValueError
<br><br>It returns a new matrix with changed rows
---
mul_matrix_row_scale(a, num, index, do_copy=True) - this function multiplies a matrix row by a scalar
* a - the matrix
* num - the scalar
* index - the index
* do_copy - boolean argument, if it is true, function won't change matrix a and make a copy, else it will change matrix a.
<br><br>If the matrix columns length are different or the matrix rows length less than index or index less than 0, it'll return a ValueError.
<br><br>It returns a new matrix - result of product a matrix row by a scalar.
---
add_matrix_row(a, b, index_a, index_b, do_copy=True) - this function summarizes two matrix rows by their indexes
* a - the first matrix
* b - the second matrix
* index_a - the index of the first matrix
* index_b - the index of the second matrix
* do_copy - boolean argument, if it is true, function won't change matrix a and b and make a copy, else it will change matrix a.
<br><br>If matrices columns length are different or matrices rows length are different or indexes are incorrect, it'll return a ValueError
<br><br>It returns a new matrix - sum of these matrices.
---
sub_matrix_row(a, b, index_a, index_b, do_copy=True) - this function substracts two matrix rows by their indexes
* a - the first matrix
* b - the second matrix
* index_a - the index of the first matrix
* index_b - the index of the second matrix
* do_copy - boolean argument, if it is true, function won't change matrix a and b and make a copy, else it will change matrix a.
<br><br>If matrices columns length are different or matrices rows length are different or indexes are incorrect, it'll return a ValueError
<br><br>It returns a new matrix - sub of these matrices.
---
create_new_row(a, new_row, do_copy=True) - this function creates a new row in the end of a matrix
* a - the matrix
* new_row - the new row of the matrix (list)
* do_copy - boolean argument, if it is true, function won't change matrix a and make a copy, else it will change matrix a.
<br><br>If the matrix columns length are different, it'll return a ValueError.
<br><br>It returns a new matrix with the new row.
---
del_row(a, index, do_copy=True) - this function deletes a row in a matrix by an index.
* a - the matrix
* index - the row's index
* do_copy - boolean argument, if it is true, function won't change matrix a and make a copy, else it will change matrix a.
<br><br>If the matrix columns length are different or the index is incorrect, it'll return a ValueError.
<br><br>It returns a new matrix without deleted row.
---
count_determinant(a) - this function counts a matrix determinant.
* a - the matrix
<br><br>If this matrix isn't square, it'll return a ValueError.
<br><br>It returns a number - determinant of the matrix.
