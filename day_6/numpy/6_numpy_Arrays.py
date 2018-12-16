import numpy

#creating an arrar
my_list1 = [1,2,3,4]
my_array1 = numpy.array(my_list1)

print(my_list1)
print(my_array1)

my_list2 = [11,22,33,44]

#creating a list of lists -> matrix
my_lists = [my_list1, my_list2]
my_matrix = numpy.array(my_lists)

print(my_matrix)

#checking the dimensions
print(my_matrix.shape)

print(my_matrix.dtype)

#creating zero fill arrays
print(numpy.zeros(5))

print(numpy.ones([5, 5]))

#empty array
print(numpy.empty(5))

#identity matrix
print(numpy.eye(5))

#a range array
print(numpy.arange(5))
print(numpy.arange(5,50, 2))