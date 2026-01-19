#.remove(), removes first occured specified items
fruits = ["banana", "apple", "cherry", "date", "orange","kiwi", "mango", "cherry", "apple"]
fruits.remove("cherry") #Removes first occurrence of cherry

#remove all cherries from the list
while "cherry" in fruits:
    fruits.remove("cherry")
print(fruits) #Prints ['banana', 'apple', 'date', 'orange', 'kiwi', 'mango', 'apple']

#.pop() removes item at specified index, if index not specified removes last item
fruits = ["banana", "apple", "cherry", "date", "orange"]

fruits.pop() #Removes last item (orange)
fruits.pop(1) #Removes item at index 1 (apple)
print(fruits) #Prints ['banana', 'apple', 'cherry', 'date']

#.del() also deletes specified index, but deletes the list from existence if index not specified

#.clear() Clears the whole list. the list will still exist but be empty
fruits.clear()
print(fruits) #Prints []