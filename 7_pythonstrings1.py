# Single line string
a = "Hello"
b = 'World'
print(type(a))
print(type(b))

# Multiline line string
poem = '''Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.'''
print(poem)
print(type(poem))

# Access string character as an Array
name = "Rajesh"
print(name[2])

# Looping through string
newName = "Kunal"
for i in newName:
    print(i)

# String Length 
print("Length of newName: ", len(newName))

# Check String
sentence = "Hello Everyone, welcome to into Python language world!"
print("welcome" in sentence)

if "Python" in sentence:
    print("Yes, 'Python' is present!")