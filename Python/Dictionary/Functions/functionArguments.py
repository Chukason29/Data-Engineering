#function definition parameters must be equal to function call arguments

def fullName(fname, sname, oname):
    print(f"My name is {fname.upper()} {sname.upper()}, {oname.upper()}")

fullName("Ebuka", "Alaegbu", "victor")

#function with keywords.
def myCountry(country = "Nigeria"):
    print(f"My country is {country}")

myCountry("USA") #outputs USA
myCountry("Australia") #outputs Australia
myCountry() # outputs Nigeria,because there is a default value during definition

#When you mix positional arguments with keywords arguments, positional arguments must come first
#before keyword arguments

#A function can take any data type as an argument (list, tuples, dicts, bools, etc)

#Positional only

#If in any case you want only position arguments in a  func, add a foward slash at the end.
def myFunction(name, /):
   pass

#for KW args only, put "* at the beginning"
def ourFunction(*, name):
    pass

# *args and **kwargs

def sumAll (*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)

sumAll(1,2,3,4,5)
sumAll(1,2,3,4,5,6,7,8,9)
sumAll(1,2,3,4,5,6,7,8,9,8,7,6,5,4)