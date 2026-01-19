#use .copy() to duplicate a list

myList = ["benz", "Audi", "BMW", "Volkswagen", "Toyota"]
carList = myList.copy()

print(carList)

#Or use the slice operator ":"
#myLists= ["banana", "apple", "cherry", "date", "orange","kiwi", "mango"]
newList = myList[:]
print(newList)