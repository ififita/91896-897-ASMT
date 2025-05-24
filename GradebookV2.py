#this program is version 2 of a student gradebook manager
from easygui import*
#dictionary to store all the student data
students = {}
def add_student(students):
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

#calling functions to run them
add_student(students)


    
    
