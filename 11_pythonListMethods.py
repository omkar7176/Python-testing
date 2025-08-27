# List Methods:
'''
append(x) ---> Add item x to the end of the list
extend(iter) ---> Extend list by appending elements from iterable
insert(i, x) ---> Insert item x at index i
remove(x) ---> Remove first occurrence of value x
pop([i]) ---> Remove and return item at index i (default: last)
sort() ---> Sort the list in-place
reverse() ---> Reverse the list in-place
'''
# append() - it will add only 1 value, only 1 arguments for append.
fruit = ["Mango", "Guava"]
fruit.append("Cherry")
print(fruit)

# insert() - it will insert new item on that index number.
name = ["om","shyam","ram"]
name.insert(1, "kunal")
print(name)

# extend()
fruit1 = ["Apple", "kiwi"]
fruit2 = ["Mango", "grapes"]
fruit1.extend(fruit2)
print(fruit1)

# remove()
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
newName.remove("kamesh")
print(newName)

# pop() - remove by specified Index
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
newName.pop(3)
print(newName)

# - Remove last items from list
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
newName.pop()
print(newName)

# Using del keyword for specified index
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
del newName[1]
print(newName)

# deleting the list completly
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
del newName
print(newName) # NameError: name 'newName' is not defined

# Clear the List
newName = ["yogesh", "jayesh", "kamesh", "shubh", "raj"]
newName.clear()
print(newName)
#OP: []