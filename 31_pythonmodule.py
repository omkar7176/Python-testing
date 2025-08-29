# A file containing a set of functions you want to insert that functions in your codebase.

# Created a Module in mymodule.py file, and we call the function in our file
import mymodule

mymodule.greeting("Omkar")
# OP: Hello Omkar


# Variables in Module
import mymodule

a = mymodule.person1["name"]
print(a)
print(type(a))

# Renaming the module name using alias
import mymodule as mm
a = mm.person1["country"]
print(a)

# Instead of importing whole module, we can import only specific function which is needed
from mymodule import person1
a = person1["age"]
print(a)