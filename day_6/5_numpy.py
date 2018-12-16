import numpy

list = [1,2,3,4]
vector = numpy.array(list)
matrice = numpy.array([list, list])

print(list)
print(vector)
print(matrice)

#creare vectori in numpy
vector_valori_0 = numpy.zeros(10)
matrice_valori_1 = numpy.ones((3,5))
matrice_identitate = numpy.eye(5)

print(vector_valori_0)
print(matrice_valori_1)
print(matrice_identitate)

print(matrice_identitate * 5)

vector_generat = numpy.arange(0,20,2)
print(vector_generat)

maxim_vector = numpy.max(vector_generat)
print(maxim_vector)

vector_random = numpy.random.randn(10)
print(vector_random)
matrice_random = numpy.random.randn(5,5)
print(matrice_random)

mattrice_valori_pozitive = numpy.where(matrice_random > 0, matrice_random, 0)

print(mattrice_valori_pozitive)