import pickle

file = open('data.dat', 'wb')
values = ['Bucuresti', 'Brasov', 'Cluj', 'Iasi']
pickle.dump(values, file)
file.close()

file = open('data.dat', 'rb')
print(pickle.load(file))
