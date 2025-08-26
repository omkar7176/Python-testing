#many values to multiple variables
a = "Omkar"
b = "Kunal"
c = "Shubh"

a, b, c = "Omk", "rahul", "shub"
print(a)
print(b)
print(c)

name = a = b = c = "Shubham"
print("Name is:", name)

fruits = ["orange", "grapes", "mango"]
a, b, c = fruits
print("The a is:", a)
print("The b is:", b)
print("The c is:", c)

# Output variables

print(a, b, c)   # must use it
print(a + b + c) # it will not add the space by default. because its concatenation