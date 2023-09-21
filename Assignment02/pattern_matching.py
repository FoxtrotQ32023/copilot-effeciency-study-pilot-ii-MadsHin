# Create function that reads line from a file
# If the line is an int then store that int and fetch the next lines equal to the int and store those in a list

# Importing the re module
import re

# Function to read the file and store the lines in a list
def read_file(file_name):
    # Opening the file
    file = open(file_name, "r")
    # Reading the file and storing the lines in a list
    lines = file.readlines()
    # Closing the file
    file.close()
    # Returning the list
    return lines

# Function that determines whether a line consists solely of an integer or not
# And returns that integer if it is


def is_int(line):
    # If the line is an integer then return True
    if re.match(r"^\d+$", line):
        return True
    # Else return False
    else:
        return False

# Function that divides the list into sublists based on the integers in the list and returns the sublists


