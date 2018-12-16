import numpy
import pandas
from pandas import Series, DataFrame

valori = [1,2,3,4,5]
serie_date = Series(valori)

populatie = [1883425, 324576, 319279, 371871]
orase = ['Bucuresti','Cluj','Timisoara','Iasi']

serie_populatie_orase = Series(populatie,orase)

print(valori)
print(serie_date)

print(serie_populatie_orase)
print("Populatie Bucuresti = {}".format(serie_populatie_orase['Bucuresti']))

data_frame = pandas.read_csv('date.csv')

print(data_frame.columns)
print("***************")
print(data_frame.info())
print("***************")
print(data_frame)

#adaugare coloana noua
data_frame['Coloana noua'] = 100
print(data_frame)
print(data_frame['Year'])

print(data_frame.where(data_frame['Year']>2010))