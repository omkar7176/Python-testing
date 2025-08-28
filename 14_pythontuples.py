'''
Tuple: Tuple is immutable in nature so by default tuple have less methods 
like count() and index().
But you can convert tuple into list and apply the list methods to tuple as well, and
then again covert it into tuple.
'''
a = ("cherry", "grapes", "mango")
print(a)

# tuple Length
a = ("cherry", "grapes", "mango")
print(len(a))

# Create the tuple with one item
b = ("Omkar",)
print(type(a)) # OP: <class 'tuple'> 

# Not a tuple
b = ("Omkar")
print(type(b)) # OP: <class 'str'>

# Tuple Items - Data type(int, String, boolean, float)
n = (1,2,3,4,5)
s = ("Jay", "vijay", "shubh")
b = (True, False, True)
f = (10.2, 23.4, 54.5)
print(n)
print(s)
print(b)
print(f)

# Tuple can contain different data type
ele = (10, "Omkar", 4.4, True)
print(ele)

# Tuple() Constructor
element = tuple(("Hello", 3.4, 23, True))
print(element)
print(type(element))

# Access tuple items using indexing
element = tuple(("Hello", "World", 3.4, 23, True))
print(element[1])

# Access tuple through slicing
fruit = ("mango", "grapes", "watermelon", "cherry", "orange", "kiwi", "chiku", "jackfruit", "apple")
print(fruit[-1]) # last item
print(fruit[2:5])
print(fruit[:3]) # How many items you want -> will print 1st 3 items
print(fruit[1:]) # skip 1st item and print all items
print(fruit[-6:-3])
print(fruit[:-2])
print(fruit[-3:])

# Check if the item exists
fruit = ("mango", "grapes", "watermelon", "cherry", "orange", "kiwi", "chiku", "jackfruit", "apple", "Omkar")
if "Omkar" in fruit:
    print("Yes, 'Omkar' is present.")

# Very Important - Changing the value of tuples, it replace the value.
fruits = ("mango", "grapes", "watermelon", "cherry", "orange", "kiwi", "chiku", "jackfruit", "apple", "Omkar")
print(type(fruits))
y = list(fruits)
print(type(y))
y[1] = "Python"
fruits = tuple(y)
print(fruits)
print(type(fruits))

# Add items in tuple (Very Important) using append() method, it attach the value
fruits = ("mango", "grapes", "watermelon", "cherry", "orange", "kiwi", "chiku", "jackfruit")
print(type(fruits))
a = list(fruits)
print(type(a))
a.append("Apple")
fruits = tuple(a)
print(fruits)
print(type(fruits))

# Adding tuple to tuple
a = ("apple", "cherry")
b = ("grapes", "kiwi")
a += b
print(a)


# Removing items from a tuple
fruits = ("mango", "grapes", "watermelon", "cherry", "orange", "kiwi", "chiku", "jackfruit")
print(type(fruits))
a = list(fruits)
print(type(a))
a.remove("mango")
fruits = tuple(a)
print(fruits)
print(type(fruits))

# How to delete tuple
fruits = ("mango", "grapes", "watermelon", "cherry", "orange", "kiwi", "chiku")
del fruits

# Packing a tuple (when we assign a values to tuple)
a = ("omkar", "rahul", "shubh")

# Unpacking the tuple (when we extract the value from the tuple)
a = ("omkar", "rahul", "shubh")
(green, yellow, red) = a
print(green)
print(yellow)
print(red)

print("--------------------------------------------------------")

# How to assign the rest of the values in tuple
a = ("omkar", "rahul", "shubh", "rajesh", "mukesh")
(green, yellow, *red) = a
print(green) # OP: omkar
print(yellow) # OP: rahul
print(red) # OP: ['shubh', 'rajesh', 'mukesh']
