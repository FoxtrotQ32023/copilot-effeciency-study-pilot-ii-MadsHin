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

def get_problems(line_list):
    # Creating an empty list to store the problems
    problems = []
    # Looping through the lines in the list
    for i, line in enumerate(line_list):
        # If the line is an integer then store the next lines in a list
        if is_int(line):
            # Creating an empty list to store the next lines
            problem = line_list[i+1:i+int(line)+2]
            
            # Appending the list to the problems list
            problems.append(problem)
    
        
        
    
    # Returning the problems list
    return problems

# function that solves the problems

def solve_problem(file_name):

    #clear the file
    open("output.ans", "w", encoding="utf8").close()

    lines = read_file(file_name)

    problems_list = get_problems(lines)

    for problem in problems_list:

        #Set the last value in the list as the string to search in
        string_to_search_in = problem[-1].strip()

        phrases_to_search_for = [phrase.strip() for phrase in problem[:-1]]

        for phrase in phrases_to_search_for:
            # create a list to store the indexes of the found words
            index_list = []
            # loop through the string to search in
            for i in range(len(string_to_search_in)):
                # if the phrase is found in the string, append the index to the list
                if string_to_search_in[i:i+len(phrase)] == phrase:
                    index_list.append(i)

                        
            # write the indexes to a file on a single line with a space between each index
            # if the word is not found, write \n to the file
            # the line cannot end with a space. So the last index in the list is written without a space

            if len(index_list) > 0:
                with open("output.ans", "a", encoding="utf8") as file:
                    for index in index_list[:-1]:
                        file.write(str(index) + " ")
                    file.write(str(index_list[-1]) + "\n")
            else:
                with open("output.ans", "a", encoding="utf8") as file:
                    file.write("\n")