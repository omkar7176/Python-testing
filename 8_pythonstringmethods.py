# UpperCase method - upper()
fullName = "omkar tupere"
print(fullName.upper())

# Lowercase method - lower()
fullName = "OMKAR TUPERE"
print(fullName.lower())

# Removing white space - strip()
greet = "       Welcome in Python Programming       " 
print(greet.strip())

# Replace String - replace()
message = "Hello Everyone"
print(message.replace("Everyone", "World"))

#Split String
'''split() method splits a string into a list. You can specify the separator,
default separator is any whitespace.'''
string = "one!two!three"
words = string.split('!')
print(words)

# Concatenation Strings
fname = "Omkar"
lname = "Tupere"
flname = fname +" "+lname
print(flname)

# wrong method to do Concatenation(Don't do it)
age = 21
myName = "Omkar"
# print(myName +" "+ age) #TypeError: can only concatenate str (not "int") to str

# Use format() method for Concatenation.
age = 22
myName = "Kunal age is {}"
print(myName.format(age))

# Unlimited arguments in strings in format() method
rollNo = 23
pincode = 411011
deptNo = 5
myMsg = "The student roll numb is {0}, address pin {1}, in deptNo is {2}."
print(myMsg.format(rollNo, pincode, deptNo))

# Removing any trailing symbol - rstrip()
message = "Hello World !!!!!!"
print(message.rstrip('!'))