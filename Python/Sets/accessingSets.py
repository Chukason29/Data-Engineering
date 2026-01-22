#Sets unordered, unchangeable*, and unindexed. and can't hold duplicate items


fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print(fruits)

#A set can contain multiple datatypes

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#True and 1 are considered a duplicate value hence

nextSet = {"apple", "banana", "cherry", False, True, 0}
print(nextSet) #False and 0 is considered the same value:

#you cannot access an item in a set my indexing it. You loop through to access the items
for x in fruits:
    print(x, end=", ")