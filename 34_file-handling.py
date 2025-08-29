# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
# "x" - Create - will create a file, returns an error if the file exists


# Write to an Existing File using 'a' mode - append()
with open("testfile.txt", "a") as f:
    f.write("Now file has more content by omkar")

with open("testfile.txt", "rt") as f:
    print(f.read())


# Overwrite Existing Content using 'w' mode - write()
with open("testfile.txt", "w") as f:
    f.write("Now file has new content by Shubham")

with open("testfile.txt", "rt") as f:
    print(f.read())


# Create a New File
f = open("newfile.txt", "x")