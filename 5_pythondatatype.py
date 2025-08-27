# Built-in data types
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set
Boolean Type:	bool
'''
a = "Omkar Tupere" #str
a = 10 #int
a = 10.7 #float
a = 2 + 2j #complex
a = ["Omkar", "Tupere"] #List
a = ("hello", "world") #tuple
a = range(5)
a = {"name": "Omkar", "City": "Mumbai"} #dict
a = {"Apple", "is", "an", "fruit"} #set
a = True #bool
print(a)
print(type(a))


# Setup the specific data type
b = str("Omkar")
b = int(20)
b = float(23.5)
b = complex(2+3j)
b = list(("Mango", "Apple"))
b = tuple(("Grapes", "kiwi"))
b = dict(name="rahul", age=22)
b = set(("cat", "dog", "horse"))
b = bool(10)

print(b)
print(type(b))
