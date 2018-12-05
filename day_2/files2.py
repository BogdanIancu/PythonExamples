f = open('test.txt', 'w')
f.write('Some random value \n')
f.write('Something else')
vb = [1,2,3,45]
f.close()

f = open('test.txt', 'r')
print(f.read())
print(f.read())
print(len(f.read()))
f.close()

f = open('cities.txt', 'r')


cities = []
for line in f:
    cities.append(line.strip())

print(cities)

