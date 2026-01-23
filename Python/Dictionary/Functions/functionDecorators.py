#A decorator is extends the behaviour of a function without changing the code

#A decorator function has three parts

#define the decorator function with the base function (func)as the argument
#define the the wrapper function within it 
#within the wrapper function, call the argument of the decorator function (which is the base function) and work on it
#on the decorator function, return the 

#using decorator to print out a number only if the that number is an even number

import math

#decorator function
def isPerfectSquare(func):
    def wrapper(number):
        if func(number) % 2 == 0:
            print ("number is even")
        else:
            print ("number is odd")
    return wrapper

#get number
@isPerfectSquare
def getNumber(n):
    return n

getNumber(10)

"""
Objective: Control access to functions.

Task:
==>Create a decorator called login_required that:

==>Checks if a global variable is_logged_in is True

==>If True, allow the function to run

==>If False, print "Access denied. Please log in."

Apply it to:

view_dashboard()

make_payment()

📌 Focus: Function wrapping, conditional logic in decorators
"""
is_logged_in = False
def login_required(func):
    def wrapper():
        if is_logged_in == False:
            print("Access denied. Please log in.")
            return
        func()
    return wrapper



@login_required
def view_dashboard():
    print("Welcome to dashboard!!")

view_dashboard()