# Sort by Alphabetical order
name = ["fhk", "ecf", "abs", "cdj", "bcs", "dog"]
name.sort()
print(name)

# Sort the list Numerically
numb = [99, 22, 45, 67, 23, 78]
numb.sort()
print(numb)

# Sorting the List in Descending Order, you can do it Alphabetical Order as well
number = [1,2,3,4,5,6,7,8,9]
number.sort(reverse=True)
print(number)

# Reverse the List using reverse() method
fruit = ["mango", "grapes", "watermelon", "cherry", "banana", "orange", "kiwi"]
fruit.reverse()
print(fruit)

# Copy a List
fruit1 = ["mango", "grapes", "watermelon", "orange", "kiwi"]
fruit2 = fruit1.copy()
print("Fruit 2 copied List", fruit2)

# Make the copy list with built in method
fruit1 = ["mango", "grapes", "watermelon", "orange", "kiwi"]
a = list(fruit1)
print("Copied by built-in method", a)

# Joining the List & also we can add using append() & also we can add using extend()
a = ["Hello World"]
b = [1, 2, 3, 4, 5]
c = a + b
print(c)

# using append() with loop
for i in b:
    a.append(i)
print(a)