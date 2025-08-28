# How to change the value of the dictionary.
emp1 = {
    "Name": "Omkar",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2021,
}
emp1["Year"] = 2016
print(emp1)
# OP: {'Name': 'Omkar', 'Age': 21, 'Position': 'Developer', 'Country': 'India', 'Year': 2016}

# update() method -> Use for add and update the values 
emp1 = {
    "Name": "Omkar",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2021
}
emp1.update({"Year": 2025})
print(emp1)
# OP: {'Name': 'Omkar', 'Age': 21, 'Position': 'Developer', 'Country': 'India', 'Year': 2025}

# How to add the items in dictionary
emp1 = {
    "Name": "Omkar",
    "Age": 21,
    "Position": "Developer"
}
emp1["color"] = "white"
print(emp1)
# OP: {'Name': 'Omkar', 'Age': 21, 'Position': 'Developer', 'color': 'white'}

# Adding the items with update() methods
emp1 = {
    "Name": "John",
    "Age": 21,
    "Position": "Developer"
}
emp1.update({"Country": "USA"})
print(emp1)
# OP: {'Name': 'John', 'Age': 21, 'Position': 'Developer', 'Country': 'USA'}

# Removing items from the dictionary
emp1 = {
    "Name": "John",
    "Age": 21,
    "Position": "Developer"
}
emp1.pop("Age")
print(emp1)

# Removing Last Inserted item
emp1 = {
    "Name": "Satwik",
    "Age": 21,
    "Position": "Developer",
    "City": "Delhi"
}
emp1.popitem()
print(emp1)
# OP: {'Name': 'Satwik', 'Age': 21, 'Position': 'Developer'}

# del keyword removes items from dictionary
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Delhi"
}
del emp1["Position"]
print(emp1)
# OP: {'Name': 'Raj', 'Age': 21, 'City': 'Delhi'}

# del keyword can also delete the whole dictionary
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Delhi"
}
# del emp1

# clear() method is used to make the empty dictionary
emp1 = {
    "Name": "Raj",
    "Age": 21,
    "Position": "Developer",
    "City": "Delhi"
}
a = emp1.clear()
print(a) # OP: None
