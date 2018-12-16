import numpy

array = numpy.arange(0,11)
print(array[8])
print(array[0:5])
array[0:5] = 100
print(array)

#it's always shallow copy
slice_array = array[0:6]
print(slice_array)
slice_array[:] = 99
print(slice_array)
print(array)

#creating a copy of an array
copy_array = array.copy()
print(copy_array)
copy_array[:] = 90
print(copy_array)
print(array)

#creating a 2 by 3 matrix
matrix = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)

print(matrix[1])
print(matrix[1][1])
print(matrix[:2, 1:])

#iterating
matrix_2d = numpy.zeros([10,10])
length = matrix_2d.shape[1]
for i in range(length):
    matrix_2d[i] = i

print(matrix_2d)

#fancy indexing
print(matrix_2d[[2,3,7,8]])