fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

fruits1, fruits2, fruits3, fruits4, fruits5, fruits6, fruits7 = fruits
print(fruits4)

(x, *y) = fruits
print(y) #outputs ['banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']