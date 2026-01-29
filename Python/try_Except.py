# the try....Except is used to catch errors

#syntax
try:
    #tests code for error
    pass
except:
    #handles the error, termintes the process if error is found
    pass
else:
    #allows you to execute the code if there is no error 
    pass
finally:
    #allows you to execute irrespective of th try...Except block
    pass

try:
    number = input("enter a number")
except ZeroDivisionError:
    print("you cant divide by zero")
except ValueError:
    print("print only numbers please")
finally:
    print("shut the program")