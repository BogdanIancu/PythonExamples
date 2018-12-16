import numpy
import matplotlib.pyplot as plt

points = numpy.arange(-5, 5, 0.01)

dx, dy = numpy.meshgrid(points, points)

print(dx)

z = (numpy.sin(dx) + numpy.sin(dy))

print(z)

plt.imshow(z)
plt.colorbar()
plt.title("Plot for sin(x) + sin(y)")

plt.show()

#input('press <ENTER> to continue')

#numpy where
A = numpy.array([1,2,3,4])
B = numpy.array([100,200,300,400])

condition = numpy.array([True, True, False, False])

#list comprehension
answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A, B, condition)]

print(answer)

#same with where
answer2 = numpy.where(condition, A, B)
print(answer2)


from numpy.random import randn

array = randn(5,5)
print(array)

print(numpy.where(array < 0, 0, array))
