#You can replace elements in a list by specifying the index and assigning a new value.
fruits = ["banana", "apple", "cherry", "date", "oranges","kiwi", "mango"]
print(fruits[3]) #Prints date
fruits[3] = "Guava"
print(fruits[3]) #Prints Guava


#change the 4th to 6th items with one value
fruits[3:6] = ["Pineapple"]
print(fruits) #Prints ['banana', 'apple', 'cherry', 'Pineapple', 'mango']