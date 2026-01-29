#Every python file is a module
#use import to import variables, methods, functions from a module

import range

print(dir(range)) #outputs every variable, function, methods etc in that module

#If you do not want to import a whole module, use from to get the particular stuff needed.

from range import myRange

print(len(myRange))