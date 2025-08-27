'''
List have the features like Ordered, Indexed, Mutable, Duplicates Allowed, 
Heterogeneous Elements, Use Case(Ordered collection of items, frequently changed)
'''

# Create python List
a = ["apple", "grapes", "mango"]
print(a)
print(type(a))

# Duplicates values can add in List
fruit = ["apple", "grapes", "mango", "apple"]
print(fruit)

# list length
print(len(fruit))

#List items - Data Types
a = ["om", "shyam", "ram"]
b = [1,2,3,4,5]
c = [True, False, True]
d = [10.2, 12.23, 3.14] 

# A List can contain String, int, bool and float
dataTypes = [10, "Omkar", True, 10.00]
print(dataTypes)
print(type(dataTypes))

# List() constructor
data = list((11, "Shubham", True, 80, "Male"))
print(data)
print(type(data))

# Accessing items from List using Index.
name = ["yogesh", "jayesh", "kamesh"]
print(name[1])

# Slicing
'''
1. Slicing from start
2. Slicing from end
3. Between two items
4. Negative slicing
  - from start
  - from end
  - between two items
'''

# To check the items in List
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
if "shubh" in newName:
    print("Yess, 'Shubh' is in the List.")

# Change the Item Value of List
nameList = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
nameList[1] = "Rahul"
print(nameList)

# Change the Item value in Range in List
fruitList = ["apple", "grapes", "mango", "kiwi", "chiku"]
fruitList[1:3] = "orange", "cherry"
print(fruitList)

# Change of 1 value by replacing with 2 values
fruitList = ["apple", "grapes", "mango", "kiwi", "chiku"]
fruitList[1:2] = ["Orange", "Guava"]
print(fruitList)
# OP: ['apple', 'Orange', 'Guava', 'mango', 'kiwi', 'chiku']

# Change 2 values by replacing with 1 value.
fruitList = ["apple", "grapes", "mango", "kiwi", "chiku"]
fruitList[1:3] = ["watermelon"]
print(fruitList)
# OP: ['apple', 'watermelon', 'kiwi', 'chiku']