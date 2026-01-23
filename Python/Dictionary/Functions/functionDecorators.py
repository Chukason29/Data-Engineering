#A decorator is extends the behaviour of a function without changing the code

#A decorator function has three parts

#define the decorator function with the base function (func)as the argument
#define the the wrapper function within it 
#within the wrapper function, call the argument of the decorator function (which is the base function) and work on it
#on the decorator function, return the 

#using decorator to print out a number only if the that number is an even number

import math
import time
import functools 

# The below is the best way to wrap stuff

def decorator_function(func): # 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #all you want your wrapper to do
        func(*args, **kwargs)
    return wrapper


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

"""
2. Execution Time Tracker

Objective: Measure performance.

Task:
*Create a decorator time_it that:
*Records how long a function takes to execute
*Prints the execution time in seconds

Apply it to:

A function that sorts a large list

A function that sleeps for a few seconds

📌 Focus: Using time module + decorator syntax
"""
def time_it(func):
    def wrapper(myList):
        start_time = time.time()
        func(myList)
        end_time = time.time()
        print (f"execution time = {end_time - start_time}")
    return wrapper

@time_it
def sortList(myList):
    myList.sort()
    return myList

theList = [3,11,1,4,56,12,17,35,60,34,100,23,99,54,135,34,23,90,51,19]
sortList(theList)



"""

3. Input Validation Decorator

Objective: Enforce argument rules.

Task:
Create a decorator validate_positive_numbers that:

Ensures all positional arguments passed to a function are positive numbers

If any value is negative, print an error and stop execution

Apply it to:

calculate_area(length, width)

calculate_salary(hours, rate)

📌 Focus: *args, argument inspection inside decorators
"""
def validate_positive_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            if i < 0:
                return("Kindly input a positive number")
        return func(*args, **kwargs)
    return wrapper    

@validate_positive_numbers
def calculate_area(length, width):
    return f"Area is = {length * width}"

print(calculate_area(-4, 6))

"""

Function Call Counter

Objective: Track function usage.

Task:
Create a decorator count_calls that:

Counts how many times a function has been called

Prints the call count each time the function runs

Apply it to:

send_email()

process_order()

📌 Focus: Closures + decorator state
"""
def count_calls(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} called {count} times")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def send_email():
    return ("email sent")

for i in range(6):
    send_email()