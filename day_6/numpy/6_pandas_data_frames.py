import pandas
from pandas import Series, DataFrame

#load the data frame from the .csv file
nfl_df = pandas.read_csv('nfl.csv')
print(nfl_df.head())
print(nfl_df.info())
print(nfl_df.columns)

print(nfl_df['Rank'])


import numpy
import matplotlib.pyplot
import seaborn

#histograma 
seaborn.catplot('Won', data=nfl_df, kind='count' )
matplotlib.pyplot.show()

#adauga o colona noua
nfl_df['New column'] = 'No value'
print(nfl_df)