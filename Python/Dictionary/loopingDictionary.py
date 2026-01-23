mycar ={
    "name": "Benz",
    "model": "C320",
    "color": "White"
}

#looping through the keys
for x in mycar.keys():
    print (x)

#looping through values
for x in mycar.values():
    print(x)

#looping through key:value pair
for x, y in mycar.items():
    print(f"{x} : {y}")