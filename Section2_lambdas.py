
#######################
#lambda expressions

sum = lambda a,b: a+b

result = sum(2,3)

print('The result is '+str(result))

def sum_function(a, b):
    return a+b

result = sum_function(2,3)

print('The result is '+str(result))

#map function
def square(value):
    return value*value

values = [1,2,3,4,5]

#using classic approach
for value in values:
    print(square(value))

#######################
#using a map
for value in map(square, values):
    print(value)


cm_per_inch = 2.54

def convert_to_centimeter(inch_value):
    return inch_value*cm_per_inch

def convert_to_inch(cm_value):
    return cm_value / cm_per_inch


centimeters = [100, 34, 2.54, 50]
inches = [23.6, 5, 6.89, 1]

print(centimeters)

#converting cm to inch
print('\n Inch values:')
for cm in centimeters:
    inch = convert_to_inch(cm)
    #print('The value of {} cm is = {:.2f} inch'.format(cm,inch))
    print('{:.2f}'.format(inch))

#using map 
print('\n Inch values:')
for inch in map(convert_to_inch, centimeters):
    print('{:.2f}'.format(inch))


#######################
# using maps and lambdas

inch_values = list(map(lambda x: x*cm_per_inch, inches))
print(inch_values)


doubled_values = list(map(lambda x: x*2,values))
print(doubled_values)

# can be used to extract data
names = ['John', 'Alice', 'Bob']
initials = list(map(lambda x: x[0], names))

print(initials)


#######################
# using maps with multiple lists

values1 = [1,2,3,4]
values2 = [10,20,30]

print('############# Processing 2 lists:')
print(values1)
print(values2)
for value in map(lambda x ,y: x+y,values1,values2):
    print(value)



#######################
# using filter

print('############# Using filters:')


values = [1, 3, 8, 4, 13, 16]

def isEven(value):
    if(value%2 == 0):
        return True
    else:
        return False

even_values = list(filter(isEven,values))

#using lambdas
even_values = list(filter(lambda x: x%2==0,values))


print(even_values)


#######################
# using reduce

import functools
print('############# Using reduce:')

result = functools.reduce(lambda x,y: x+y, [47,11,42,13])

print("Reduction result is "+str(result))

#######################
# using list comprehension

centimeters_values = [ (x*cm_per_inch) for x in inches]
print(centimeters_values)

centimeters_values = [ (x*cm_per_inch) for x in inches]
print(centimeters_values)


values = [1,5,4,8,10,13]
even_values_pow = [(x**2) for x in values if x%2 == 0]
print(even_values_pow)


some_values = [(x, y**2, z**3) for x in range(1,5) for y in range(1,5) for z in range(1, 5)]
print(some_values)


