# All methods of Dictionary
# pop()
# clear()
# update()
# get()
# keys()
# values()
# items()
# popitem()
# copy()


# loop through dictionary
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Mumbai"
}
for i in emp1:
    print(i) # OP: It will print only keys of the dictionary.

# With loop print all the values in the dictionary
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Mumbai"
}
for i in emp1:
    print(emp1[i]) # OP: It will only print all the values

# values() method to return value of dictionary.
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Mumbai"
}
for i in emp1.values():
    print(i)

# keys() method to return value of a dictionary.
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Mumbai"
}
for i in emp1.keys():
    print(i)

# Best, Now loop through both the keys and values, by using the items() method.
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Mumbai"
}
for i,y in emp1.items():
    print(i, y)
# OP: 
# Name Raj
# Age 21
# Position Developer
# City Mumbai    

# copy() method is used to copy the one dict.
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Mumbai"
}
newdict = emp1.copy()
print(newdict)
# OP: {'Name': 'Raj', 'Age': 21, 'Position': 'Developer', 'City': 'Mumbai'}

# Another way to make a copy is use dict() built in function.
emp1 = {
    "Name": "Raj",
    "Age": 22,
    "Position": "Developer",
    "City": "Mumbai"
}
emp2 = dict(emp1)
print(emp2)
# OP: {'Name': 'Raj', 'Age': 22, 'Position': 'Developer', 'City': 'Mumbai'}

# Nested dictionary, a dict can able to contain another dictionary.
info = {
    "address1" : {
        "city": "Bengaluru",
        "pin": 1111
    },
    "address2" : {
        "city": "Mumbai",
        "pin": 1112
    },
    "address3" : {
        "city": "Delhi",
        "pin": 1113
    }
}
print(info) 

# Append the multiple dictionary in single dictionary
address1 = {
    "city": "Bengaluru",
    "pin": 1111
},
address2 = {
    "city": "Mumbai",
    "pin": 1112
},
address3 = {
    "city": "Delhi",
    "pin": 1113
},
newAddress = {
    "address1" : address1,
    "address2" : address2,
    "address3" : address3
}
print(newAddress)