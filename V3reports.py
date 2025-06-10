from easygui import *
from V3students import students, calc_avg
from datetime import date

def print_summary():
    if not students:
        msgbox("No student data found.")
        return
    #getting the date
    today = date.today()
    report = "Student Gradebook Summary Report\n"
    report += f"Date: {today}\n"
    report += "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n" 
    
    for name, subjects in students.items():
        report += f"{name}'s scores:\n"
        for sub, score in subjects.items():
            report += f" {sub}: {score}\n"
        avg = calc_avg(list(subjects.values()))
        #+= to add a value to a variable
        report += f" Average: {avg:.2f}\n"
        report += "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
    
    msgbox(report, "Gradebook Summary")
    #appending to the external file
    with open("student_grades.txt", "a") as student_grades_file:
        student_grades_file.write(report)
       
