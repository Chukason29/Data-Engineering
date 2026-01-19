name = "Victor" #global variable

def myName():
    name = "John" #local variable
    print(f"local name is: {name}")

def globalName():
    global name
    print(f"global name inside function is: {name}")

globalName()
myName()

print(f"global name is: {name}")