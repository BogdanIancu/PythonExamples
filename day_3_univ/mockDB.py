import shelve

db = shelve.open('secure')
db["name"]='Gigescu'
db["surname"]='Popel'
db.close()

db = shelve.open('secure')
values = dict(db)
for (k, v) in values.items():
    print('{}: {}'.format(k, v))

db.close()