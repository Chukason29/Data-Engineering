#multiline string example
multiline_string = """This is an example of a multiline string.
It can span multiple lines.dsvfvfvsdfvdsfsfvsfvdsfv
sdvfsdfvdfvsdfvdsfvdfv
vsdfvsdfvsdfvdsfvsdfvsdfsdfvfvsdvfd
"""
print(multiline_string)

#N/B A string is also an array

name =  "Data Engineering"
print(name[-1])  #prints last character i.e g
for i in name:
     print(i, end=" * ")

#String's length
print("\nLength of the string is:", len(name))

#checking if a string is within a string  ==> use "in" or "not in" appropriately
if "Data" in name:
    print("Yes, 'Data' is present in the string.")