#You can join list either concatenating lists
#using .append()
#using .extend() Note==> Doesn't returna new list

#concatenation 

list1 = ["Ben", "Jane", "Kate", "Grace"]
list2 = ["Ifeoma", "Uche", "Chioma", "Ebuka"]

list3 = list1 + list2
print(list3)

list1.extend(list2)
list3.sort()
print(list3)
