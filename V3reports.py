'''This is the reports module for version 3 of the Student Gradebook Manager.
It imports student data and calculates averages.
It generates and displays a summary report of all students.
'''
from easygui import *
from V3students import students, calc_avg #Import the student data dictionary and average function
from datetime import date #Import to get the date

def print_summary():
    #If there are no students in the dictionary
    if not students:
        msgbox("No student data found.")
        return
    #Getting the date
    today = date.today()
    
    report = "Student Gradebook Summary Report\n"
    report += f"Date: {today}\n"
    report += "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n" 

    #Looping through each student in the dictionary
    for name, data in students.items():
        student_class = data.get("class","Unknown")
        report += f"{name} (Tutor Class: {student_class})\n"

        #Getting the student's subjects and scores
        subjects = data.get("subjects",{})
        for sub, score in subjects.items():
            report += f" {sub}: {score}\n"

        #Calculating and adding the average score
        avg = calc_avg(list(subjects.values()))
        #Using += to add a value to a variable
        report += f" Average: {avg:.2f}\n"
        report += "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"

    #Displaying the complete report in a textbox
    textbox("Student Gradebook Summary", "Student Gradebook Summary", report)
    
