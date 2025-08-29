# Creating and calling a function
def my_function():
    print("Hello, Welcome in the Python Programming")

my_function()

# Arguments - arguments are specified inside the function parentheses.
def name(fname):
    print("Hello", fname)

name("Omkar")
name("Shuhbham")
name("Kunal")

# Number of Arguments - 2 args
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Omkar", "Tupere")

# Arbitrary Arguments, *args
def my_function(*subject):
    print("The 1st rank student is: " + subject[0])
    print("The 2nd rank student is: " + subject[1])

my_function("Omkar", "Shubham", "Kunal", "Rajesh","Somesh")

# Keyword Arguments key=value pair
def my_function(apple, grapes, banana):
    print("The color of apple is " + apple)
my_function(apple = "red", grapes = "green", banana = "yellow")

# Arbitrary keyword arguments **kwargs
def my_function(**kids):
    print("His last name is "+ kids["lname"])
my_function(fname = "monu", lname = "pandey")

# Default Parameter value
def my_function(country="India"):
    print("I am from "+ country)
my_function("UK")
my_function()
my_function("Spain")

# Passing list as an argument
def print_list(items):
    for i in items:
        print(i)

my_list = [1, 2, 3, 4, 5]
print_list(my_list)

# Return values - To let a function return a value then you use return statement
def my_function(x):
    return 5 * x
print(my_function(4))
print(my_function(5))
print(my_function(6))

# Pass Statement
def my_function():
    pass