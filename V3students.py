'''this is a module for version 3 that will be imported from the main module.
This module contains the code for all the options'''
from easygui import *
#dictionary to store all the student data
students = {}

def add_student():
    #asking for the user details
    while True:
        name = enterbox("Enter the student's full name: ")
        if name is None:
            return #returning to the main menu
        name = name.strip()
        #checking for any integers or blanks in the name
        if name == "":
            msgbox("This can't be left blank.")
        elif name.isdigit():
            msgbox("Names cannot contain numbers.")
        elif name in students:
            msgbox("That student already exists.")
        else:
            break
    #asking how many subjects the user wants to enter scores for
    while True:
        subject_num = enterbox("How many subjects are you entering scores for?")
        if subject_num is None:
            return
        try:
            subject_num = int(subject_num)
            break #exiting the loop if valid
        except ValueError:
            msgbox("Enter a valid whole number.")

    subjects = {} #storing the subjects in a dictionary
    for i in range(subject_num):
        #asking for the entries in a multenterbox
        while True:
            field_names = ["Subject name:", "Score (0-100):"]
            entry = multenterbox(f"Enter subject {i+1} info for {name}:","Subject Entry", field_names)
            if entry is None:
                return
            subject, score = entry[0].strip(), entry[1].strip()
            if subject == "":
                msgbox("Subject name can't be blank.")
                continue
            elif subject.isdigit():
                msgbox("Subject names can't be numbers.")
                continue
            elif subject in subjects:
                msgbox("You've already entered that subject. Please enter a different subject.")
                continue
            try:
                score = int(score)
                if score <0 or score >100:
                    msgbox("Score must be between 0 and 100.")
                else:
                    subjects[subject] = score
                    break
            except ValueError:
                msgbox("Please enter a valid whole number.") 
    students[name] = subjects
    msgbox(f"{name} has been added successfully.")

def search_student():
    #asking for a student's name to search in the dictionary
    name = enterbox("Enter the student's name to search: ")
    if name in students:
        subjects = students[name]
        scores = list(subjects.values())
        #calculating their average score
        avg = calc_avg(scores)
        #creating a string to show each subject and its score
        subject_scores = ', '.join(f"{sub}: {score}" for sub, score in subjects.items())
        msgbox(f"{name}'s scores: {subject_scores}\nAverage: {avg:.2f}")
    else:
        msgbox("Student not found.")
#creating a function to allow user to edit information
def edit_info():
    name = enterbox("Enter the student’s name to edit:")
    if name is None or name not in students:
        msgbox("Student not found.")
        return
    option = buttonbox(f"What would you like to edit for {name}?", choices=["Edit name", "Edit subject score", "Cancel"])
    if option == "Edit name":
        edited_name = enterbox("Enter the new name:")
        if edited_name is None:
            return
        edited_name = edited_name.strip() #removing extra spaces from the name
        if edited_name == "": #check if the new name is empty
            msgbox("This can't be blank.")
        #making sure the name doesn't contain numbers
        elif any(char.isdigit() for char in edited_name):
            msgbox("Names can't have numbers.")
        #check if the name already exists
        elif edited_name in students:
            msgbox("That name already exists.")
        else:
            #updating the dictionary key
            students[edited_name] = students.pop(name)
            msgbox(f"Name changed to {edited_name}.")

    elif option == "Edit subject score":
        #getting the list of subjects for the student
        subjects = students[name]
        if not subjects:
            msgbox("No subjects found.")
            return
        subject_list = list(subjects.keys())#showing the list of subject names
        if len(subject_list) == 1:
            chosen_subject = subject_list[0]
        else:
            chosen_subject = choicebox("Choose a subject to edit:", choices=subject_list)
        if chosen_subject is None:
            return

        new_score = enterbox(f"Enter new score for {chosen_subject}:")
        if new_score is None:
            return
        #try to convert it to a number
        try:
            new_score = float(new_score)
            if not new_score.is_integer() or new_score < 0 or new_score > 100:
                msgbox("Score must be a whole number between 0 and 100.")
            else:
                subjects[chosen_subject] = int(new_score)
                msgbox("Score updated.")
        except ValueError:
            msgbox("Invalid score entered.")
        msgbox("Score changed successfully")
def delete_student():
    student_list = list(students.keys())
    if len(student_list) == 0:
        msgbox("There are no students to delete.")
        return
    elif len(student_list) == 1:
        name = student_list[0]
    else:
        name = choicebox("Select a student to delete", choices = student_list)
        if name is None:
            return
    confirm = ynbox(f"Are you sure you would like to delete {name}?")
    if confirm:
        del students[name]
        msgbox(f"{name} has been deleted.")
    else:
        msgbox("Deletion has been cancelled.")
        
def calc_avg(scores):
    return sum(scores) / len(scores) if scores else 0

def save_students():
    with open("students_grades.txt", "w") as student_grades_file:
        for name, subjects in students.items():
            studen  t_grades_file.write(f"Student: {name}\n")
            for subject, score in subjects.items():
                student_grades_file.write(f"{subject}: {score}\n")
            student_grades_file.write("\n")

def load_students():
    global students
    students = {} #reset
    try:
        with open("students_grades.txt", "r") as student_grades_file:
            name = ""
            for line in file:
                line = line.strip()
                if line.startswith("Student:"):
                    name = line.replace("Student:", "").strip()
                    students[name] = {}
                elif ":" in line and name:
                    subject, score = line.split(":")
                    students[name][subject.strip()] = int(score.strip())
    except FileNotFoundError:
        students = {}
                         
