#.add() adds a single item to a set

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
fruits.add("pear")

print(fruits)

#.update() is used to add the items of another set ot Iterable to the give set

cars = {"benz", "bmw", "ford"}
fruits.update(cars)
print(fruits)