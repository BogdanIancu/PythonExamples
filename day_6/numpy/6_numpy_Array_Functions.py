import numpy

array = numpy.arange(10)
print(numpy.sqrt(array))

random_array = numpy.random.randn(10)
print(random_array)

print(numpy.add(array, random_array))

print(numpy.maximum(array, random_array))