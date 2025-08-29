# The "try" block lets you test a block of code for errors.

# The "except" block lets you handle the error.

# The "else" block lets you execute code when there is no error.

# The "finally" block lets you execute code, regardless of the result of the try and except blocks.

# Example
try:
    num = int(input("Enter a number: "))
    result = 50 / num
except Exception as e:
    print("Error: ", e)
else:
    print("Result: ", result)
finally:
    print("Execution of code completed")

# NOTE: 
# 1. If user enters 0, a ZeroDivisionError is caught.
# 2. If user enters "abc", a ValueError is caught.



# raise - Manually trigger an exception using in function(Custom Exceptions)
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is set to", age)

set_age(-5)  # This will raise a ValueError
