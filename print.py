import os 
import tempfile
import datetime

#define date to be te current date and time exclusing microseconds
date = datetime.datetime.now()

finaldate = date.strftime("%Y-%m-%d %H:%M:%S")



#define directory path
directory_path = 'C:\\Users\\DJche\\OneDrive\\Documents\\projects\\print via wifi\\temp files'

user_input = input("What would you like to print? ")

# Create a temporary file within the specified directory
with tempfile.NamedTemporaryFile(dir=directory_path, mode='w', delete=False, suffix='.txt') as temp_file:
    temp_file.write(finaldate + "\n" + "\n" + user_input)
    temp_file_path = temp_file.name

# Print the directory path
print("print in progress!")

# Set the variable files to the path of the temporary file
files = temp_file_path

# Open the file for printing
os.startfile(files, "print")
