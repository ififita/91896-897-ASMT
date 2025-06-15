#This program is version 2 of a student gradebook manager
from easygui import*
#Dictionary to store all the student data
students = {}
#Defining constants
MIN_SCORE = 0
MAX_SCORE = 100

def add_student():
    #asking for user details
    while True:
        name = enterbox("Enter the student's full name: ")
        if name is None:
            return #returning to the main menu
        name = name.strip()
        #checking for any integers or blanks in the name
        if name == "":
            msgbox("Please type something (this can't be left blank).")
        elif name.isdigit():
            msgbox("Please try again – numbers are not allowed in this field.")
        elif name in students:
            msgbox("A student with that name already exists. Please enter another name.")
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
            elif subject.isdigit():
                msgbox("Please try again – numbers are not allowed in this field.")
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
                if not score.is_integer():
                    msgbox("Please enter an integer (ie: a number which does not have a decimal part).")
                elif score < MIN_SCORE:
                    msgbox(f"Please enter an integer that is more than (or equal to) {MIN_SCORE}.")
                elif score > MAX_SCORE:
                    msgbox(f"Please enter an integer that is less than (or equal to) {MAX_SCORE}.")
                else:
                    score = int(score)
                    break
            except ValueError:
                msgbox("Please enter a valid number for the test score.")
        subjects[subject] = score #storing the subject and score in the dictionary
    students[name] = subjects #saving the students subjects and scores in the main students dictionary
    msgbox(f"{name} has been added successfully.\n")#adding a new line for better formatting

def calc_avg(scores):
    #if score list is empty, return 0 to avoid dividing by zero
    if not scores:
        return 0
    #if not, add all scores and divide by the number of scores
    return sum(scores)/len(scores)
    
def print_summary():
    if not students: #using if not operator to check for empty dictionary
        msgbox("Sorry, no student data has been entered.")
        return
    report = ""
    for name, subjects in students.items():
        scores = list(subjects.values())
        avg = calc_avg(scores)
        #concatenating subjects and scores 
        subject_scores = ','.join(f"{sub}:{score}" for sub, score in subjects.items())
        report += (f"{name}'s scores: {subject_scores} | Average Score: {avg:.2f}\n\n")
        report += "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n\n"
    msgbox(report,"Student Gradebook Summary")
    
    
def search_student():
    #asking for a student's name to search in the dictionary
    name = enterbox("Enter a student name to search: ")
    if name in students:
        subjects = students[name]
        scores = list(subjects.values())
        #calculating their average score
        avg = calc_avg(scores)
        #creating a string to show each subject and its score
        subject_scores = ','.join(f"{sub}:{score}" for sub, score in subjects.items())
        msgbox(f"{name}'s scores: {subject_scores} | Average Score: {avg:.2f}")
    else:
        msgbox("Student not found.")
#creating a function to allow user to edit information
def edit_info():
    name = enterbox("Enter the name of the student to edit their info: ")
    if name is None or name not in students:
        msgbox("Student not found.")
        return
    option = buttonbox(f"What do you want to edit for {name}?",choices = ["Edit name", "Edit a subject score", "Cancel"])
    if option == "Edit name":
        edited_name = enterbox("Enter the edited name: ")#asking for the new name
        if edited_name is None:
            return
        edited_name = edited_name.strip() #removing extra spaces from the name
        if edited_name == "": #check if the new name is empty
            msgbox("Please type something (this can't be left blank).")
            return
        #making sure the name doesn't contain numbers
        if any(char.isdigit() for char in edited_name):
            msgbox("Please try again – numbers are not allowed in this field.")
            return
        #check if the name already exists
        if edited_name in students:
            msgbox("A student with that name already exists.")
            return
        #updating the dictionary key
        students[edited_name] = students.pop(name)
        msgbox(f"Name has been changed from {name} to {edited_name}.")
        
    elif option == "Edit a subject score":
        #getting the list of subjects for the student
        subjects = students[name]
        if not subjects:
            msgbox("Sorry, no subjects have been entered for this student.")
            return
        subject_names = list(subjects.keys()) #showing the list of subject names
        if len(subject_names) == 1:
            edited_sub = subject_names[0]
        else:
            edited_sub = choicebox("Which subject would you like to edit?", choices=subject_names)
        if edited_sub is None:
            return
        while True:
            new_score = enterbox(f"Enter the edited score for {edited_sub}: ")
            if new_score is None:
                return
            #try to convert it to a number
            try:
                new_score = float(new_score)
                if not new_score.is_integer():
                    msgbox("Please enter an integer (i.e., a number with no decimal part).")
                elif new_score < MIN_SCORE:
                    msgbox(f"Please enter an integer that is more than or equal to {MIN_SCORE}.")
                elif new_score > MAX_SCORE:
                    msgbox(f"Please enter an integer that is less than or equal to {MAX_SCORE}.")
                else:
                    subjects[edited_sub] = int(new_score)
                    break
            except ValueError:
                msgbox("Invalid score entered. Please enter a number.")       
        msgbox("Score changed successfully.")
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
            quit()
#calling the main function to display the menu
main()
            
        
        


    
    
