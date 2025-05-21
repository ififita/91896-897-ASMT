#this program is version 1 of a student gradebook manager
students = {} #storing the student details in a dictionary
while True:
    #displaying the menu options
    print("\nStudent Gradebook Manager") 
    print("1. Add a student")
    print("2. Display a summary report")
    print("3. Search for a student")
    print("4. Exit")
    option = input("Please choose an option (1-4): ")
    
    if option == "1":
        while True:
        #asking for user details
            name = input("Enter the student's name: ")
            #using .isdigit()to check for any integers in the input
            if name.strip() == "" or any(char.isdigit() for char in name):
                    print("Please enter a valid name (no numbers or empty values). ")
            else:
                break
        subjects = {} #storing the students subjects and scores in a dictionary
        while True:
            subject = input(f"Enter the subject for {name}. Type 'done' to finish: ")
            if subject.lower() == "done": #exiting the while loop once "done" has been entered
                break
            score = input(f"Enter {name}'s test score for {subject}: ")
            try:
                score = float(score) #converting the score to float using type conversion
                subjects[subject] = score
            except ValueError:
                print("Please enter the score as an integer.")
        students[name] = subjects

    elif option == "2": 
        if not students: #using if not operator to check for empty dictionary
            print("Sorry, no student data has been entered.")
        else:
            print("\nSummary Report")
            for name, subjects in students.items():
                scores = list(subjects. values())
                average = round(sum(scores) / len(scores), 2) #calculating the average score
                #concatenating subjects and scores 
                subject_scores = ', '.join(f"{sub}:{score}" for sub, score in subjects.items())
                print(f"{name}'s scores: {subject_scores} | Average Score: {average}")
    elif option == "3":
        print("Student Search")
        name = input("Enter a student name to search: ")
        if name in students:
             average = round(sum(scores) / len(scores), 2) #calculating the average score
             #concatenating subjects and scores 
             subject_scores = ', '.join(f"{sub}:{score}" for sub, score in subjects.items())
             print(f"{name}'s scores: {subject_scores} | Average Score: {average}")
        else:
            print("Student not found.")
    elif option == "4":
        print("The Gradebook Manager is exiting. Goodbye!")
        quit()
        break #exiting out of the loop 
    else:
        print("Invalid option. Please enter 1 - 4.")


        
        

            
            
        
    
            
            
               
