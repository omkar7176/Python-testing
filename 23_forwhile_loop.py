# For loop and while loop

# While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

# While loop with break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# While loop with continue statement
i = 1
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)    

# the else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")