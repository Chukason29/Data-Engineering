# Looping through a list for loop
#for loop is used for definite iteration, when the number of iterations is known.

fruits = ["banana", "apple", "cherry", "date", "orange","kiwi", "mango"]

#if you need a numerical looping, do the first for loop else do the second for loop

for i in range(len(fruits)):
    print(fruits[i])  # Accessing each item using index

for i in fruits:
    print(f"\n{i}")  # Accessing each item directly

#While loop is used when the number of iterations is not known, it continues until a certain condition is met.

count = 0

while count < len(fruits):
    print(f"I love: {fruits[count]}")
    count = count + 1

