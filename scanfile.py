#Import os module
from __future__ import print_function
import os


# Ask the user to enter string to search
search_path = raw_input("Enter directory path to search : ")
file_type = raw_input("File Type : ")
search_str = raw_input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("\\") or search_path.endswith("\\") ): 
        search_path = search_path + "\\"
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path ="."

print (search_path)

# Repeat for each file in the directory  
for fname in os.listdir(search_path):

   # Apply file type filter   
   if fname.endswith(file_type):

        # Open file for reading
        with open(search_path + fname) as fo:

        # Read the first line from the file
            line = fo.readline()

        # Initialize counter for line number
            line_no = 1

        # Loop until EOF
            while line != '' :
                # Search for string in line
                    index = line.find(search_str)
                    if ( index != -1) :
                        print(fname, "[", line_no, ",", index, "] ", line, sep="")

                # Read next line
                    line = fo.readline()  

                # Increment line counter
                    line_no += 1
 
