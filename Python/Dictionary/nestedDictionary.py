child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#To get the name of child3
print(myfamily["child3"]["name"])

for key, value in myfamily.items():
    print(f"{key} : \n")
    for sub_key in value:
        print(f"{sub_key}: {value[sub_key]}")