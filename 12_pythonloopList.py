# Note: Loop, we use the "range" and "len"
# 1. Loop through List
fruit = ["mango", "grapes", "watermelon", "cherry"]
for i in fruit:
    print(i)
#OP: Same output as below 2.    


# 2. Loop through the index number
fruit = ["mango", "grapes", "watermelon", "cherry"]
for i in range(len(fruit)):
    print(fruit[i])
#OP: Same output as above 1.


# 3. using a while loop
fruit = ["mango", "grapes", "watermelon", "cherry"]
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1
#OP: Same output as above 2.

# 4. List comprehension
fruit = ["mango", "grapes", "watermelon", "cherry", "banana", "orange", "kiwi"]
newList = []

for i in fruit:
    if "a" in i:
        newList.append(i)
print(newList)
# OP: ['mango', 'grapes', 'watermelon', 'banana', 'orange']    