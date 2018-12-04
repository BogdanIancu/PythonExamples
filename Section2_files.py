import pickle

#pickle example
cities = ["Paris", "London", "Athens", "Sofia"]
countries = ["France","England","Greece", "Bulgaria"]

capitals = (cities, countries)

#serialize the list of cities
fh = open("data.pkl", "bw")
pickle.dump(capitals, fh)
fh.close()


#deserialize
f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes)


#shelve example

import shelve

s = shelve.open("MyShelve")
s["street"] = "Calea Dorobanti"
s["city"] = "Bucharest"

print(s["street"])

s["street"] = "Magheru"

print(s["street"])

s.close()

s = shelve.open("MyShelve")

myData = dict(s)

print(myData)
