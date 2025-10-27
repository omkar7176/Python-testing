'''
NOTE: When we don't need to create a third variable, it makes the changes in the original variable set.
AND when we create a third variable, it does not modify the original set of items.
'''
#All Methods of Sets:
# add()
# update()
# union()
# remove()
# discard()
# pop()
# clear()
# del
# intersection_update()
# intersection()
# symmetric_difference_update()
# symmetric_difference()

# Adding set items using add()
fruit = {"mango", "grapes", "cherry", "orange", "kiwi", "chiku", "jackfruit"}
fruit.add("apple")
print(fruit)

# How to attach two sets using update()
name1 = {"omkar", "kunal"}
name2 = {"Shubh", "Raj"}
name1.update(name2) # no need to create the 3rd variable
print(name1)

# How to join the 2 sets using the union() method.
set1 = {'a', 'b', 'c', 'd'}
set2 = {1, 2, 3, 4, 5}
set3 = set1.union(set2) # Need to create the 3rd variable
print(set3)

# How to remove the items from set using remove()
nameList = {"Raj", "kunal", "Shubh", "omkar"}
nameList.remove("kunal")
print(nameList)

# discard() for removing items in set
color = {"white", "black", "yellow", "green", "blue"}
color.discard("black")
print(color)

# Remove the last items using the pop(), method will give you the wrong output.
color = {"white", "black", "yellow", "green", "blue"}
color.pop()
print(color)

# clear() method is used to empty the set
color = {"white", "black", "yellow", "green", "blue"}
color.clear()
print(color)
# OP: set()

# The del keyword is used to delete the set completely
color = {"white", "black", "yellow", "green", "blue"}
del color
# print(color)

# How to loop through the set
color = {"white", "black", "yellow", "green", "blue", "purple", "red", "grey"}
for i in color:
    print(i)

# Print only duplicate items from both sets using the intersection_update() method
set1 = {"white", "black", "yellow", "green", "blue"}
set2 = {"black", "yellow", "white", "purple", "grey"}
set1.intersection_update(set2)
print(set1)
# OP: {'black', 'yellow', 'white'}

# Print only duplicate items from sets using the intersection() method, but need to create a new variable.
set3 = {"white", "black", "yellow", "green", "blue"}
set4 = {"black", "yellow", "white", "purple", "grey"}
set5 = set3.intersection(set4) # Need to create the 3rd variable
print(set5)

# IMP: By default set cannot add duplicate items, but we have a method as well,
# using symmetric_difference_update()
set6 = {"white", "black", "yellow", "green", "blue"}
set7 = {"black", "yellow", "white", "purple", "grey"}
set6.symmetric_difference_update(set7)
print(set6)

# symmetric_difference() method will return a new set that contain only the elements that contain only the elements that are NOT present in Both sets. --> same as symmetric_difference_update().
setold = {"white", "black", "yellow", "green", "blue"}
setnew = {"black", "yellow", "white", "purple", "grey"}
set = setold.symmetric_difference(setnew) # need to create 3rd variable
print("from sym_differ", set)
