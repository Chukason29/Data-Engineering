#recursive functions are functions that call themselves within themselves.

#solving factorial using loops
def factorial (n):
    fact = 1
    for n in range(1,n+1):
        fact = fact * n
    return fact

print(factorial(5))

#using loops, get the number of an identified fibonnacci series

def fibSeries(n):
    count = 0
    fibList = []
    x, y = 0, 1
    while count <= n:
        fibList.append(x)
        x, y = y, x + y
        count += 1
        
    return fibList

print(fibSeries(7))