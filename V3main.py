'''this is the main module which imports the V3students and V3reports files.
the functions and modules are called here.'''
from easygui import *
#Importing the other files
import V3students
V3students.load_students()
import V3reports

def main():
    while True:
        #Printing the main menu with button choices
        choice = buttonbox("Welcome to the Student Gradebook Manager! Please choose an option to get started.",
                           choices=[
                               "Add a Student",
                               "Display a Summary Report",
                               "Search for a Student",
                               "Edit Student Info",
                               "Delete a Student",
                               "Exit"
                           ])
        #Calling the function based on the user's choice
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
            V3students.save_students()#Saving the student data before exiting
            msgbox("Exiting the Gradebook Manager. Goodbye!")
            break #Exiting the main loop and ending the program
        
#Making sure the main() function only runs when this file is run directly     
if __name__ == "__main__":
    main()
