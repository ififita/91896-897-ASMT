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
    
    for name, data in students.items():
        student_class = data.get("class","Unknown")
        report += f"{name} (Tutor Class: {student_class})\n"
        subjects = data.get("subjects",{})
        for sub, score in subjects.items():
            report += f" {sub}: {score}\n"
        avg = calc_avg(list(subjects.values()))
        #+= to add a value to a variable
        report += f" Average: {avg:.2f}\n"
        report += "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
    
    msgbox(report, "Gradebook Summary")
    
