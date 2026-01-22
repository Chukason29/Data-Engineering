#Tuples are ordered hence, they are indexed
#They are unchangeable, You can't remove or add an item after the tuple has been created
#tuple can contain different data types

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