#Tuples are ordered hence, they are indexed
#They are unchangeable, You can't remove or add an item after the tuple has been created
#tuple can contain different data types
#It can duplicate values

#Creating Tuples

myTuple = ()
print(type(myTuple)) # tuple
#OR
tupleList = tuple()
print(type(tupleList)) # tuple

#To create a tuple with just one item, a comma must be added to it hence python wont see it as a tuple
oneItemTuple = (5,)
print(type(oneItemTuple))

#A tuple can contain different data types

itemTuple = ("Banana", 5, [1,2,3], 4, 3.6, True)
print(itemTuple)

for x in itemTuple:
    print(x, end=", ")

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#.count() get the number of times a particular item occur in the tuple
print(fruits.count("cherry"))

#.index() gets the position of a specified item
print(fruits.index("mango"))

i = 0
for i in range(len(fruits)):
    if i == 0:
        continue
    if i%2 != 0:
        print (fruits[i], end=", ")
    else:
        continue

#A dice game