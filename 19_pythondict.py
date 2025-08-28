'''
Dictionary: Ordered✅ || Indexed✅ || Mutable✅ || Heterogeneous Elements ✅ ||
            Duplicates Allowed❌(keys must be unique)
           : we store the items in dict in key:value pairs.
           : make sure keys must be unique, values can duplicates. 
'''
# Dictionary
emp1 = {
    "Name": "Rahul",
    "Age": 22,
    "Position": "Developer",
    "Country" : "India"
}
print(emp1)
print(type(emp1))

# If you want print the value of key e.g. "Position"
emp1 = {
    "Name": "Kunal",
    "Age": 25,
    "Position": "Developer",
    "Country" : "India"
}
print(emp1["Position"])

# Duplicates are not allowed,(it will override the key)
emp1 = {
    "Name": "Omkar",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2021,
    "Year": 2023
}
print(emp1["Year"])
# OP: 2023 ---> (keys must be unique, values can duplicate)

# How to find dictionary length
emp1 = {
    "Name": "Shubh",
    "Age": 26,
    "Position": "Developer"
}
print(len(emp1)) # OP: 3

# find the dictionary length, when you have duplicate keys
emp1 = {
    "Name": "Omkar",
    "Age": 21,
    "Country" : "India",
    "Year" : 2021,
    "Year": 2023
}
print(len(emp1)) # OP: 4 (it will skip the duplicate key, and consider it only one)

# Dict items - Data types with list as well
stud = {
    "name": "Rajesh",
    "Age": 22,
    "marks": 98.32,
    "passed": True,
    "subject": ["maths", "chem", "phy","bio"]
}
print(stud)

# Accessing items of Dictionary
stud = {
    "name": "Rajesh",
    "Age": 22,
    "marks": 98.32,
    "passed": True,
    "subject": ["maths", "chem", "phy","bio"]
}
x = stud["marks"]
print(x)

# Accessing items of dictionary through get() method
emp1 = {
    "Name": "Omkar",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2021
}
x = emp1.get("Name")
print(x)

# key() method, will return all the keys which are present in the dictionary.
emp1 = {
    "Name": "Yogesh",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2025
}
b = emp1.keys()
print(b)
# OP: dict_keys(['Name', 'Age', 'Position', 'Country', 'Year'])

# Adding the new key with value in original dictionary
emp1 = {
    "Name": "Saket",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2025
}
print("Before:", emp1)
emp1["color"] = "White"
print("After:", emp1)

# values(), how to get the values from the dictionary
emp1 = {
    "Name": "Saket",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
    "Year" : 2025
}
val = emp1.values()
print(val)
# OP: dict_values(['Saket', 21, 'Developer', 'India', 2025])

# Adding the new value to the existing key in original dictionary
emp1 = {
    "Name": "Saket",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
}
emp1["Position"] = "DevOps Engineer"
print(emp1)
# OP: {'Name': 'Saket', 'Age': 21, 'Position': 'DevOps Engineer', 'Country': 'India'}

# How to get each items in a dictionary as tuples in the dictionary
emp1 = {
    "Name": "Saket",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
}
val = emp1.items()
print(val)
# OP: dict_items([('Name', 'Saket'), ('Age', 21), ('Position', 'Developer'), ('Country', 'India')])

# Check if the key exists
emp1 = {
    "Name": "Saket",
    "Age": 21,
    "Position": "Developer",
    "Country" : "India",
}
if "Country" in emp1:
    print("Yess, country is present")