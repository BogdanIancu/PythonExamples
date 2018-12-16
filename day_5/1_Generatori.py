
def functie_generare_valori_pare(maxim):
  valori = []
  valoare = 0
  for i in range(int(maxim/2)):
    valoare += 2
    valori.append(valoare)
  return valori

def generator_valori_pare(maxim):
  valoare = 0
  for i in range(int(maxim/2)):
    valoare += 2
    yield valoare

def generator_3_numere_pare():
  yield 2
  yield 4
  yield 6


#afisare numere pare
for valoare in functie_generare_valori_pare(20):
  print(valoare)

#afisare 3 numere pare
print("***************")
generator_numere_pare = generator_3_numere_pare()
print(generator_numere_pare)
print(generator_numere_pare.__next__())
print(next(generator_numere_pare))
print(next(generator_numere_pare))
# genereaza o exceptie de tip StopIteration
#print(next(generator_numere_pare))

for valoare in generator_3_numere_pare():
  print('Numar par = {}'.format(valoare))

print('******************')
for valoare in generator_valori_pare(20):
  print('Numar par = {}'.format(valoare))