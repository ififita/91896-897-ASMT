'''this is the main module which imports the V3students and V3reports files.
the functions and modules are called here.'''
from easygui import *
#importing the other files
import V3students
V3students.load_students()
import V3reports

def main():
    while True:
        #printing the main menu
        choice = buttonbox("Welcome to the Student Gradebook Manager! Please choose an option to get started.",
                           choices=[
                               "Add a Student",
                               "Display a Summary Report",
                               "Search for a Student",
                               "Edit Student Info",
                               "Delete a Student",
                               "Exit"
                           ])
        if choice == "Add a Student":
            V3students.add_student()
        elif choice == "Display a Summary Report":
            V3reports.print_summary()
        elif choice == "Search for a Student":
            V3students.search_student()
        elif choice == "Edit Student Info":
            V3students.edit_info()
        elif choice == "Delete a Student":
            V3students.delete_student()
        elif choice == "Exit":
            V3students.save_students()
            msgbox("Exiting the Gradebook Manager. Goodbye!")
            break
if __name__ == "__main__":
    main()
