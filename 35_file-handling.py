# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function.

import os
os.remove("newone.txt")



# Check if File exist
import os
if os.path.exists("newone.txt"):
    os.remove("newone.txt")
else:
    print("The file does not exist")


# Delete Folder
# To delete an entire folder, use the os.rmdir() method
import os
os.rmdir("myfolder")
