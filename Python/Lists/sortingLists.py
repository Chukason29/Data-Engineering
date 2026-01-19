#.sort() is the chief sorter of lists

#.sort() is case sensitive, hence it gives uppercase letters priority.
#.sort() sorts in ascending order
#.sort() sort

fruits = ["banana", "apple", "cherry", "date", "orange","kiwi", "mango"]
fruits.sort()
print(fruits)

#to sort in descending order, we do .sort(reverse = True)

#Or you do .reverse()

fruits.sort(reverse=True)
print(fruits) #reverses the sort.
