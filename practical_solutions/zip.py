# a zip több iterálható dolgot vesz elő és azonos pozícióban levő elemeket párosít össze


names = ["Anna", "Béla", "Csaba"]
ages = [24, 31, 28]

results = zip(names, ages)
# fontos -> a zip nem listát ad vissza, hanem egy ilyet :<zip object at 0x...>
for result in results:
    print(result)

# ellenben:
results2 = list(zip(names, ages))
print(results2)

# több mint 2 dolgot is lehet zippelni
cities = ["Szeged", "Budapest", "Pécs"]
results3 = list(zip(names, ages, cities))
print(results3)

# a fennmaradó, nem párosítható elemek egyszerűen kiesnek a párosításból
cars = ["Toyota", "Ford", "Kia", "Renault"]
# results4 = list(zip(names, ages, cities, cars, strict=True))
# print(results4)


# dict készítése két listából
keys = ["name", "age", "city"]
values = ["Levi", 30, "Szeged"]

dict_result = dict(zip(keys, values))
print(dict_result)