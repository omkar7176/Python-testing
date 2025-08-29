# Print each items of in list
fruit = ["mango", "grapes", "watermelon", "cherry", "apple"]
for i in fruit:
    print(i)

# Looping through string
for i in "Hello":
    print(i)

# Break Statement    
fruit = ["mango", "grapes", "watermelon", "cherry", "apple"]
for i in fruit:
    print(i)
    if i == "watermelon":
        break
# OP: mango, grapes, watermelon
# BUT
fruit = ["mango", "grapes", "watermelon", "cherry", "apple"]
for i in fruit:
    if i == "grapes":
        break
    print(i)
# OP: mango

# Continue Statement
fruit = ["mango", "grapes", "watermelon", "cherry", "apple"]
for i in fruit:
    if i == "watermelon":
        continue # continue means skip the value
    print(i)
# OP: mango, grapes, cherry, apple

# The range() function
for i in range(5):
    print(i)

# example of some deep range()
for i  in range(2, 8):
    print(i)


# You can specify value of increment by adding the 3rd parameter.
for i in range(2, 30, 3):
    print(i)


# Else in for loop
for i in range(6):
    print(i)
else:
    print("finally executed")   

# pass statement
n = int(input("Enter the numb: "))
if n == 26:
    print("Welcome")
elif n > 30 and n < 50:
    print("exit")
else:
    pass