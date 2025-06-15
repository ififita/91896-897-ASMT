'''This is the main module which imports the V4students, V4reports, and V4graph files.
All the functions are called from here to run the Student Gradebook Manager program'''
from easygui import *
#Importing the other modules
import V4students #Loading existing student data from file when the program starts
V4students.load_students()
import V4reports
import V4graph

def main():
    while True:
        #Printing the main menu with button choices
        choice = buttonbox("Welcome to the Student Gradebook Manager! Please choose an option to get started.",
                           choices=[
                               "Add a Student",
                               "Display a Summary Report",
                               "Show Student Graph",
                               "Search for a Student",
                               "Edit Student Info",
                               "Delete a Student",
                               "Exit"
                           ])
        #Calling the function based on the user's choice
        if choice == "Add a Student":
            V4students.add_student()
        elif choice == "Display a Summary Report":
            V4reports.print_summary()
        elif choice == "Show Student Graph":
            V4graph.visualise_student()
        elif choice == "Search for a Student":
            V4students.search_student()
        elif choice == "Edit Student Info":
            V4students.edit_info()
        elif choice == "Delete a Student":
            V4students.delete_student()
        elif choice == "Exit":
            V4students.save_students() #Saving the student data before exiting
            msgbox("Exiting the Gradebook Manager. Goodbye!")
            break #Exiting the main loop and ending the program
#Making sure the main() function only runs when this file is run directly     
if __name__ == "__main__":
    main()
