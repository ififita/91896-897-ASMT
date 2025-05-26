#this program is version 2 of a student gradebook manager
from easygui import*
#dictionary to store all the student data
students = {}
def add_student():
    #asking for user details
    while True:
        name = enterbox("Enter the student's name: ")
        if name is None:
            return #returning to the main menu
        name = name.strip()
        #checking for any integers or blanks in the name
        if name == "" or any(char.isdigit() for char in name):
            msgbox("Please enter a valid name (no numbers or empty values).")
        elif name in students:
            msgbox("A student with that name already exists. Try another name.")
        else:
            break
    #asking how many subjects the user wants to enter scores for
    while True:
        subject_num = enterbox(f"How many subjects are you entering scores for?: ")
        if subject_num is None:
            return
        try:
            subject_num = int(subject_num) 
            break #exiting the loop if valid
        except ValueError:
            msgbox("Please enter a valid integer for the number of subjects.")
    subjects = {} #storing the subjects in a dictionary
    #loop for each subject the user wants to enter
    for i in range(subject_num):
        #asking for a valid subject name
        while True:
            subject = enterbox(f"Enter the name of the subject {i+1} for {name}: ")
            if subject is None:
                return
            subject = subject.strip()
            if subject == "":
                msgbox("The subject name cannot be empty. Please enter a valid subject name.")
            elif subject in subjects:
                msgbox("That subject has already been entered. Please enter a different one.")
            else:
                break
        #asking for the test score for the subject
        while True:
            score = enterbox(f"Enter {name}'s score for {subject}: ")
            if score is None:
                return
            try:
                score = float(score) #converting the score to float
                break
            except ValueError:
                msgbox("Please enter a valid number for the test score.")
        subjects[subject] = score #storing the subject and score in the dictionary
    students[name] = subjects #saving the students subjects and scores in the main students dictionary
    msgbox(f"{name} has been added successfully.\n")#adding a new line for better formatting
    
def print_summary():
    if not students: #using if not operator to check for empty dictionary
        msgbox("Sorry, no student data has been entered.")
        return
    for name, subjects in students.items():
        scores = list(subjects.values())
        avg = calc_avg(scores)
        #concatenating subjects and scores 
        subject_scores = ','.join(f"{sub}:{score}" for sub, score in subjects.items())
        report = (f"{name}'s scores: {subject_scores} | Average Score: {average}")
        msgbox(report, "Summary Report")


def main():
    while True:
        #creating the main page with the options
        choice = buttonbox("Welcome to the Student Gradebook Manager! Please choose an option to get started.",
                           choices = ["Add a Student","Display a Summary Report","Search for a Student","Edit Student Info","Exit"])
        #calling each function when an option is choice
        if choice == "Add a Student":
            add_student()
        elif choice == "Display a Summary Report":
            print_summary()
        elif choice == "Search for a Student":
            search_student()
        elif choice == "Edit Student Info":
            edit_info()
        else:
            msgbox("The Gradebook Manager is exiting. Goodbye!")
            break
main()
            
        
        


    
    
