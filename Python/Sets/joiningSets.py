#.union() and .update() joins two sets. Shortcut ==> " | "
cars1 = {"benz", "audi", "mazda", "jeep", "honda", "ford", "toyota"}
cars2 = {"bmw", "honda", "JAC", "ford", "GAC", "toyota"}

cars3 = cars1.union(cars2)

print(cars3)

#.intersection() collects only similar items Shortcut = " & "
cars4 = cars1.intersection(cars2)
print(cars4)

#.difference() collects what is in the first set but not in the second set. Shortcut = " - "
cars5 = cars1.difference(cars2)
print(cars5)

#.symmetric_difference keeps all items EXCEPT duplicates. Shortcut = " ^ "
cars6 = cars1.symmetric_difference(cars2)
print(cars6)