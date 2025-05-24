#this program is version 2 of a student gradebook manager
from easygui import*
students = {}
def add_student(students):
    #asking for user details
    while True:
        name = enterbox("Enter the student's name: ").strip()
        #checking for any integers or blanks in the name
        if name == "" or any(char.isdigit() for char in name):
            msgbox("Please enter a valid name (no numbers or empty values).")
        elif name in students:
            msgbox("A student with that name already exists. Try another name.")
        else:
            break
    subjects = {} #storing the subjects in a dictionary
    while True:
        subject = enterbox(f"Enter a subject for {name}. Type 'done' to finish: ").strip()
        #using .lower() to turn all characters lowercase
        if subject.lower() == "done":
            break
        score_input = enterbox(f"Enter {name}'s score for {subject}: ")
        try:
            score = float(score_input)#converting the score to float using type conversion
            subjects[subject] = score
        except ValueError:
            msgbox("Please enter the score as a number.")
    students[name] = subjects
    msgbox(f"{name} has been added successfully.\n")#adding a new line for better formatting

#calling functions to run them
add_student(students)


    
    
