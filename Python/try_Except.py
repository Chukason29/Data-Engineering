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
    number = int(input("enter a number:"))
    print(3/number)
except ZeroDivisionError:
    print("you cant divide by zero")
except ValueError:
    print("input only numbers please")
finally:
    #this runs regardless of the output from try..except
    print("shut the program")

#NB ==> There can be a try...except block within a try....except