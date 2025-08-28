'''
Sets: Ordered❌ || Indexed❌ || Duplicates Allowed❌ ||
      Heterogeneous Elements ✅ || Mutable✅
    : It contains the Unique items.
    : add the items in set, we use {}.
'''

# What are sets? (unordered, unchangable, unindexed)
a = {"apple", "cherry", "orange"}
print(a)
print(type(a))

# duplicates are not allowed
x = {"a", "b", "c", "b"}
print(x)
# OP: {'a', 'c', 'b'}  
# Note: will not add the duplicate items. 
# and every time it will gives you a new output because it alternatively rotate.

# Get the length of the Set
name = {"omkar", "shaym", "ram", "rajesh"}
print(type(name))
print(len(name))

# A set with int, String, boolean, float all types of data
container = {10, "Omkar", True, 23.1}
print(container)
print(type(container))

# The set() constructor
word = set(("ab", "cd", "ef", "gh"))
print(word) 
print(type(word))

# How to access items in set through loop
name = {"omkar", "shaym", "ram", "rajesh"}
for i in name:
  print(i)

# Check if "rajesh" is present or not
name = {"omkar", "shaym", "ram", "rajesh"}
if "rajesh" in name:
  print("Yess, rajesh is present")
