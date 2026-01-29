#Range is a method that hold a sequence of number

#syntax ==>  range('start', 'stop', 'step')

#start ==> where the figures starts
#stop ==> where the figure end, excluding the value of the stop
#step ==> the sequence with which the number will be listed

myRange = range(1, 10, 2)
#to display a range as list, you cast it.
print(list(myRange)) #outputs [1, 3, 5, 7, 9]

#A Range can be sliced

#used len() to get the length of a range

print(len(myRange))




