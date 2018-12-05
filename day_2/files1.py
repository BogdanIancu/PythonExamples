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