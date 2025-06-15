'''this is a module for version 3 that will be imported from the main module.
This module contains the code for all the options'''
from easygui import *
#Dictionary to store all the student data
students = {}

#Defining constants
FILENAME = "student_grades.txt"
MAX_SUBJECTS = 10
MIN_SCORE = 0
MAX_SCORE = 100

def add_student():
    #Asking the user to enter student details and scores
    while True:
        field_names = ["Full name:", "Tutor Class (e.g., 12B1)"]
        entry = multenterbox("Enter student details:", "Student Info", field_names)
        if entry is None: #If the user cancels input then exit the function early
            return
        #Getting the name and class and cleaning off any extra spaces
        name, student_class = entry[0].strip(), entry[1].strip()
        #Validating student name
        if name == "":
            msgbox("Please type something (this can’t be left blank)")
            continue
        elif any(char.isdigit() for char in name):
            msgbox("Please try again - numbers are not allowed in this field.")
            continue
        elif name in students:
            #Preventing duplicate student names
            msgbox("That student has already been entered. Please enter another student.")
            continue
        #Validating tutor class
        if student_class == "":
            msgbox("Tutor class can't be left blank.")
            continue
        elif not student_class.isalnum():
            msgbox("Tutor class must be alphanumeric (e.g., 12B1).")
            continue
        elif "." in student_class:
            msgbox("Class can't contain decimals.")
            continue
        break
    while True:
        #Ask how many subjects they want to enter
        subject_num = enterbox("How many subjects are you entering scores for?")
        if subject_num is None:
            return
        try:
            subject_num = int(subject_num)
            #Validating the number of subjects within the valid range
            if subject_num < 1:
                msgbox("Please enter an integer that is more than (or equal to) 1.")
                continue
            elif subject_num > MAX_SUBJECTS:
                msgbox("Please enter an integer that is less than (or equal to) 10.")
                continue
            break  
        except ValueError:
            msgbox("Please enter an integer (ie: a number which does not have a decimal part).")

    #Dictionary to hold subject names and scores for this student
    subjects = {} 
    #Loop to get subject name and score for each subject
    for i in range(subject_num):
        while True:
            field_names = ["Subject name:", "Score (0-100):"]
            entry = multenterbox(f"Enter subject {i+1} info for {name}:","Subject Entry", field_names)
            if entry is None:
                return
            subject, score = entry[0].strip().title(), entry[1].strip()
            #Validating subject name
            if subject == "":
                msgbox("Subject name can't be blank.")
                continue
            elif subject.replace('.', '', 1).isdigit():
                msgbox("Subject names can't be numbers or decimals.")
                continue
            elif subject in subjects:
                msgbox("You've already entered that subject. Please enter a different subject.")
                continue
            #Validating score input as integer and in the valid range
            try:
                score = int(score)
                if score < MIN_SCORE or score > MAX_SCORE:
                    msgbox("Score must be between 0 and 100.")
                else:
                    subjects[subject] = score
                    break
            except ValueError:
                msgbox("Please enter a valid whole number.") 
    #Saving the new student and their subjects into the dictionary
    students[name] = {
            "class": student_class,
            "subjects": subjects
        }
    msgbox(f"{name} has been added successfully.")

def search_student():
    while True:
        #asking for a student's name to search in the dictionary
        name = enterbox("Enter the student's name to search: ")
        if name is None: 
            return
        name = name.strip() #Remove extra spaces
        if name == "":
            msgbox("Please type something (this can’t be left blank)")
            continue
        elif any(char.isdigit() for char in name):
            msgbox("Student names can't contain numbers.")
            continue #Ask again if the name has numbers
        break #Exiting the loop if the input is valid
    #Checking if the student exists in the data
    if name in students:
        student_data = students[name] #Getting student details
        student_class = student_data["class"] #Getting all subjects and scores
        subjects = student_data["subjects"] #Getting the scores list
        scores = list(subjects.values())
        if not scores:
            msgbox(f"{name} (Tutor Class: {student_class}) has no subject scores.")
            return
        avg = calc_avg(scores)
        subject_scores = '\n'.join(f"{sub}: {score}" for sub, score in subjects.items())
        msgbox(f"{name} (Tutor Class: {student_class})'s scores:\n{subject_scores}\nAverage: {avg:.2f}")
    else:
        msgbox("Student not found.")
#creating a function to allow user to edit information
def edit_info():
    while True:
        #Asking for the student's name to edit
        name = enterbox("Enter the student’s name to edit:")
        if name is None:
            return
        name = name.strip()
        if name == "":
            msgbox("Name can't be left blank.")
            continue #Ask again if empty
        elif any(char.isdigit() for char in name):
            msgbox("Names can't contain numbers.")
            continue
        break
    #Checking if the student exists
    if name not in students:
        msgbox("Student not found.")
        return
    
    option = buttonbox(f"What would you like to edit for {name}?", choices=["Edit name", "Edit subject score", "Add new subject", "Cancel"])
    if option == "Edit name":
        while True:
            #Asking for new name
            edited_name = enterbox("Enter the new name:")
            if edited_name is None:
                return
            edited_name = edited_name.strip()
            #Validating new name
            if edited_name == "":
                msgbox("This can't be blank.")
            elif edited_name == name:
                msgbox("That's the same name. Please enter a different name.")
            elif any(char.isdigit() for char in edited_name):
                msgbox("Names can't have numbers.")
            elif edited_name in students:
                msgbox("That name already exists.")
            else:
                #Confirming name change
                confirm = ynbox(f"Are you sure you want to change '{name}' to '{edited_name}'?")
                if confirm:
                    #Renaming the student in the dictionary
                    students[edited_name] = students.pop(name)
                    msgbox(f"Name changed to {edited_name}.")
                    save_students()
                else:
                    msgbox("Name change cancelled.")
                break #Exiting the loop 

    elif option == "Edit subject score":
        #getting the list of subjects for the student
        subjects = students[name]["subjects"]
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
            score = int(new_score)
            if not (MIN_SCORE <= score <= MAX_SCORE):
                msgbox(f"Score must be between {MIN_SCORE} and {MAX_SCORE}.")
            else:
                subjects[chosen_subject] = score
                msgbox(f"Score for '{chosen_subject}' updated to {score}.")
                save_students()
            # do something with score
        except ValueError:
            msgbox("Please enter a valid whole number.")
            
    elif option == "Add new subject":
        subjects = students[name]["subjects"]
        if len(subjects) >= MAX_SUBJECTS: #Limit the max subjects to 10
            msgbox(f"Sorry, you can't add more than {MAX_SUBJECTS} subjects.")
            return
        while True:
            field_names = ["Subject name:","Score (0-100):"]
            entry = multenterbox(f"Enter the new subject info for {name}:","Add Subject",field_names)
            if entry is None:
                return
            subject, score = entry[0].strip().title(), entry[1].strip()
            #Validating subject name
            if subject == "":
                msgbox("Subject name can't be blank.")
                continue
            elif subject.isdigit():
                msgbox("Subject names can't be numbers.")
                continue
            #If the subject already exists then ask if user wants to update score
            if subject in subjects:
                update = ynbox(f"'{subject}' has been added already. Would you like to update the score instead?")
                if update:
                    new_score = enterbox(f"Enter the new score for {subject}:")
                    if new_score is None:
                        return
                    try:
                        new_score = int(new_score)
                        if new_score < MIN_SCORE or new_score > MAX_SCORE:
                            msgbox("Score must be between {MIN_SCORE} and {MAX_SCORE}.")
                        else:
                            subjects[subject] = new_score
                            msgbox(f"Score for '{subject}' has been updated successfully for {name}.")
                            break
                    except ValueError:
                        msgbox("Please enter a valid whole number.")
                else:
                    continue
            else:
                try:
                    score = int(score)
                    if score < MIN_SCORE or score > MAX_SCORE:
                        msgbox("Score must be between {MIN_SCORE} and {MAX_SCORE}.")
                    else:
                       #Add the new subject and score
                        subjects[subject] = score
                        msgbox(f"Subject '{subject}' added successfully for {name}.")
                        save_students()
                        break
                except ValueError:
                    msgbox("Please enter a valid whole number.")
     

def delete_student():
    #getting a list of all student names
    student_list = list(students.keys())
    #if there are no students, show message and return
    if len(student_list) == 0:
        msgbox("There are no students to delete.")
        return
    elif len(student_list) == 1: #if only one student exists then choose that student
        name = student_list[0]
    else:
        name = choicebox("Select a student to delete", choices = student_list)
        if name is None: 
            return
    confirm = ynbox(f"Are you sure you would like to delete {name}?")
    if confirm:
        del students[name]
        msgbox(f"{name} has been deleted.")
        save_students()
    else:
        msgbox("Deletion has been cancelled.")
        
           
        
def calc_avg(scores):
    '''calculating average scores of the list if not empty
    return 0 if the list is empty to avoid division by zero'''
    return sum(scores) / len(scores) if scores else 0

def save_students():
    #open a text file to save the student data
    with open(FILENAME,"w") as file:
        #iterate over each student and their subjects dictionary
        for name, data in students.items():
            student_class = data["class"]
            subjects = data["subjects"]
            file.write("---------------------------\n")
            file.write(f"Student: {name}\n")
            file.write(f"Tutor Class: {student_class}\n")
            for subject, score in subjects.items():
                file.write(f"{subject}: {score}\n")
            #calculating and writing the average score with 2 decimal places
            avg = calc_avg(list(subjects.values()))
            file.write(f"Average score: {avg:.2f}\n")

def load_students():
    global students
    #reset the students dictionary to empty before loading new data
    students = {} 
    try:
        #open the text file and reading the student data
        with open(FILENAME, "r") as file:
            name = "" #temporary variable for student name
            student_class = ""
            for line in file:
                line = line.strip() #removing blank from the start of end of the line
                #detecting a line starting with "Student:" indicating a new student
                if line.startswith("Student:"):
                    #getting the student name from the line
                    name = line.replace("Student:", "").strip()
                    #initial empty dictionary for the students subjects
                    students[name] = {"class": "", "subjects": {}}
                #for other lines with ":" 
                elif line.startswith("Tutor Class:") and name:
                    students[name]["class"] = line.replace("Tutor Class:","").strip()
                elif ":" in line and name:
                    #skip lines that show average score info
                    if line.lower().startswith("average score"):
                        continue
                    #split the line into subject and score parts
                    parts = line.split(":")
                    if len(parts) == 2:
                        subject, score = parts
                        try:
                            students[name]["subjects"][subject.strip()] = int(score.strip())
                        except ValueError:
                            # If score is not an int, try float or skip
                            try:
                                students[name]["subjects"][subject.strip()] = int(float(score.strip()))
                            except ValueError:
                                # log or skip invalid score
                                print(f"Invalid score for {subject.strip()}: {score.strip()}")

                        
    #if file doesn't exist, keep students as an empty dictionary 
    except FileNotFoundError:
        students = {}
                         
