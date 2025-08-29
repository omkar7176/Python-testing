# File Handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# syntax: open(filename, mode)

'''
There are 5 mode.
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
'''

# Open the file using open()
f = open("demofile.txt", "rt")


# To read the file, we use the read()
f = open("demofile.txt", "rt")
print(f.read())
# NOTE: If the file is located in a different location, you will have to specify the file path.


# Using the "with" statement
with open("demofile.txt") as f:
  print(f.read())
# Then you do not have to worry about closing your files, the with statement takes care of that.


# Close Files (close the files, is the good practise when you are done with it)
f = open("demofile.txt")
print(f.read())
f.close()


# Read Lines
# You can return one line by using the readline() method. must use the readline() with keyword
with open("demofile.txt") as f:
    print(f.readline())