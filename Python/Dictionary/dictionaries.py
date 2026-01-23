#dictionaries are like objects in JavaScript.

mycar ={
    "name": "Benz",
    "model": "C320",
    "color": "White"
}

#can get items via indexing 
print(mycar["name"]) #output benz

#OR

print(mycar.get("name")) #output benz

#item can be changed
mycar["name"] = "Audi"
print(mycar["name"]) # output Audi

#duplicates are not allowed.

#.copy() copies the whole items in the dictionary to another one.