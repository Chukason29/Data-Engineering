#Local Scopes variables are variables within a function
def func():
    pi = 3.142 #local variable
    print(pi)
    
#print(pi) #This will be error

# A local variable can be accessed from a function within that function

def myFunc():
    x = 100
    def checkX():
        print(f"The number x is: {x}")
    checkX()
myFunc()