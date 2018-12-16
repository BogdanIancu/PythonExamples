import pandas
from pandas import Series,DataFrame
import numpy
import matplotlib
import seaborn

#import data intr-un DataFrame

df = pandas.read_csv('titanic.csv')
print(df.head())
print(df.info())

#analiza statistica date pasageri
seaborn.catplot('Sex',data=df, kind='count')
matplotlib.pyplot.show()

seaborn.catplot('Pclass',data=df, kind='count', hue='Sex')
# matplotlib.pyplot.show()

#definire functie care determina ce pasageri erau copii
def este_copil(pasager):
    varsta, gen = pasager
    if(varsta < 16):
        return 'child'
    else:
        return gen

#aplicam filtrul si generam o coloana noua
df['PersonType'] = df[['Age','Sex']].apply(este_copil,axis = 1)
print(df)

seaborn.catplot('Pclass',data=df, kind='count', hue='PersonType')
# matplotlib.pyplot.show()

df['Age'].hist(bins=80)
# matplotlib.pyplot.show()

print("Varsta medie era {}".format(df['Age'].mean()))

#grafic de tip kde Gen vs Varsta
grafic = seaborn.FacetGrid(df, hue="Sex",aspect=4)
grafic.map(seaborn.kdeplot,'Age', shade=True)

grafic.add_legend()
reper_start = 0
repert_final = df['Age'].max()
grafic.set(xlim=(reper_start,repert_final))
matplotlib.pyplot.show()

#grafic de tip kde Tip versoana vs Varsta
grafic = seaborn.FacetGrid(df, hue="PersonType",aspect=4)
grafic.map(seaborn.kdeplot,'Age', shade=True)

grafic.add_legend()
reper_start = 0
repert_final = df['Age'].max()
grafic.set(xlim=(reper_start,repert_final))
matplotlib.pyplot.show()

#grafic de tip kde Clasa vs Varsta
grafic = seaborn.FacetGrid(df, hue="Pclass",aspect=4)
grafic.map(seaborn.kdeplot,'Age', shade=True)

grafic.add_legend()
reper_start = 0
repert_final = df['Age'].max()
grafic.set(xlim=(reper_start,repert_final))
matplotlib.pyplot.show()

#analiza in functie de punte
info_punte = df['Cabin'].dropna()
print(info_punte.head())
nivel_punte = []
for info in info_punte:
    nivel_punte.append(info[0])

df_cabine = DataFrame(nivel_punte)
df_cabine.columns = ['Cabin']
df_cabine = df_cabine.sort_values(by='Cabin', ascending=True)
seaborn.catplot('Cabin',data=df_cabine,kind='count',palette='winter')
matplotlib.pyplot.show()

# analiza grad supravieturie
df['Supravietuitor'] = df.Survived.map({0:'no',1:'yes'})
seaborn.catplot('Supravietuitor',data=df,kind='count',palette='Set1')
matplotlib.pyplot.show()

seaborn.catplot('Pclass','Survived',data=df,kind='point', hue='PersonType')
matplotlib.pyplot.show()

seaborn.lmplot('Age','Survived', data=df)
matplotlib.pyplot.show()

seaborn.lmplot('Age','Survived', hue='Pclass', data=df)
matplotlib.pyplot.show()

seaborn.lmplot('Age','Survived', hue='Sex', data=df)
matplotlib.pyplot.show()