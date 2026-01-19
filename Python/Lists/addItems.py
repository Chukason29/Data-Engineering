#.append() adds item to the end of the list

fruits = ["banana", "apple", "cherry"]
fruits.append("orange")
print(fruits) #Prints ['banana', 'apple', 'cherry', 'orange']

#.insert() adds item at the specified index
fruits.insert(1, "kiwi") #Inserts kiwi at index 1
print(fruits[1]) #Prints kiwi

#You can add a list to another list using .extend()

list1 = ["banana", "apple", "cherry"]
list2 = ["orange", "kiwi", "mango"]

list1.extend(list2)
print(list1) #Prints ['banana', 'apple', 'cherry', 'orange', 'kiwi', 'mango']

#It can extend a tuple also
tuple1 = ("grape", "pineapple")
list1.extend(tuple1)
print(list1) #Prints ['banana', 'apple', 'cherry', 'orange', 'kiwi', 'mango', 'grape', 'pineapple']