import matplotlib
matplotlib.use('Agg')#Using a non-interactive backend to make images without showing a window
import matplotlib.pyplot as plt
from easygui import enterbox, msgbox
from V4students import students, calc_avg
import os

def visualise_student():
    #Checking if there are any students loaded
    if not students:
        msgbox("No student data found.")
        return
    #Asking the user to enter full name
    while True:
        name = enterbox("Enter the student's full name to visualize:")
        if name is None: #If user pressed cancel
            return
        name = name.strip() #Removing extra spaces
        if name == "":
            msgbox("Please type something (this can’t be left blank).")
            continue
        if name not in students:
            msgbox("Student not found. Please enter a valid student name.")
            continue
        break #Exiting the loop once valid name is entered
    #Getting the student's data
    data = students[name]
    subjects = data["subjects"]
    if not subjects: #If there are no subjects
        msgbox(f"{name} has no subjects/scores to display.")
        return

    #Preparing the data for plotting
    subject_names = list(subjects.keys())
    scores = list(subjects.values())
    avg = calc_avg(scores) #Calculating the average score

    #Creating a bar graph with subject scores
    plt.figure(figsize=(8,5))
    bars = plt.bar(subject_names, scores, color='#FFEE8C')
    #Drawing a horizontal line for average score
    plt.axhline(avg, color='red', linestyle='--', label=f'Average: {avg:.2f}')
    plt.ylim(0, 110) #Setting the y-axis limits a bit above the max score
    plt.ylabel('Score')
    plt.xlabel('Subject')
    plt.title(f"{name}'s Subject Scores")
    plt.legend()
    #Adding score labels above each bar
    for bar, score in zip(bars, scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{score}', 
                 ha='center', va='bottom')

    plt.tight_layout() #Adjusting the layout

    #Saving the plot to a temporary file
    temp_filename = "temp_plot.png"
    plt.savefig(temp_filename)
    plt.close() #Closing the plot to free memory

    #Showing the saved image in a EasyGUI message box
    msgbox(f"{name}'s Data Visualisation:", image=temp_filename)

    #Try to delete the temporary file after displaying it
    try:
        os.remove(temp_filename)
    except Exception as e:
        print(f"Could not delete temporary file: {e}")
