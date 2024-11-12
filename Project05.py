# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Tony Fernandez>,<11/13/24>, <Assignment05>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
#import .json
import json  # Importing json module for JSON file handling
FILE_NAME: str = "Enrollments.json" # Using JSON file format

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # Change from list to dict, as it holds individual student data
students: list = []  # List to store multiple student records
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
try:
    with open(FILE_NAME, 'r') as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"{FILE_NAME} not found. Starting with an empty list.")
    students = []
except json.JSONDecodeError:
    print(f"Error decoding JSON from {FILE_NAME}. Starting with an empty list.")
    students = []
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    students = []

# Present and Process the data
# Main Program Loop
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ").strip()

    # Input user data
    if menu_choice == "1":
        # Get student's first name with error handling
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
        except ValueError as e:
            print(e)
            continue

        # Get student's last name with error handling
        try:
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
        except ValueError as e:
            print(e)
            continue

        # Get course name (no error handling required as it's optional)
        course_name = input("Please enter the name of the course: ").strip()

        # Create a dictionary for the student's data
        student_data = {
            "FirstName": student_first_name,
            "LastName": student_last_name,
            "CourseName": course_name
        }

        # Add the student data to the list
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

        # Present the current data
    elif menu_choice == "2":
        if not students:
            print("No student data available.")
        else:
            print("-" * 50)
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
            print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, 'w') as file:
                for student in students:
                    json.dump(student, file)
                    file.write('\n')  # Write each student on a new line
            print("The following data was saved to file!")
            print("-" * 50)
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("Exiting the program.")
        break

    else:
        print('Invalid Option')
        print("Please select from 1 to 4.\n")

print("Program Ended")
