#this program is version 1 of a student gradebook manager
students = {} #storing the student details in a dictionary
#defining constants
MIN_OPTION = 1
MAX_OPTION = 4
while True:
    #displaying the menu options
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("Student Gradebook Manager") 
    print("1. Add a student")
    print("2. Display a summary report")
    print("3. Search for a student")
    print("4. Exit")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    #asking the user to choose a menu option
    option = input("Please choose an option (1-4): ").strip()
    #input validation with specific messages
    if option == "":
        print("Please type something (this can’t be left blank).")
        continue
    elif not option.isdigit():
        print("Please enter an integer (ie: a number which does not have a decimal part).")
        continue
    try:
        option = int(option)
        #checking if the number is within the valid menu option rage
        if option < MIN_OPTION:
            print(f"Please enter an integer that is more than (or equal to) {MIN_OPTION}.")
            continue
        elif option > MAX_OPTION:
            print(f"Please enter an integer that is less than (or equal to) {MAX_OPTION}.")
            continue
    except ValueError:
        print("Please enter an integer (i.e., a number without decimals or letters).")
        continue
    
    if option == 1:
        while True:
        #asking for user details
            name = input("Enter the student's name: ")
            #using .isdigit()to check for any integers in the input
            if name.strip() == "" or any(char.isdigit() for char in name):
                    print("Please enter a valid name (no numbers or empty values).")
            elif name in students:
                print("That student name already exists. Please enter a different name.")
            else:
                break
        subjects = {} #storing the students subjects and scores in a dictionary
        #while loop to enter multiple subjects and scores
        while True:
            while True:
                subject = input(f"Enter the subject for {name}. Type 'done' to finish: ")
                if subject.lower() == "done": #exiting the while loop once "done" has been entered
                    break
                if subject.strip() == "":
                    print("Subject name cannot be blank.")
                elif subject.isdigit():
                    print("Subject name cannot be a number. Please enter a valid subject name.")
                else:
                    break
            if subject.lower() == "done":
                break
            #getting a valid score for the subject
            while True:
                score = input(f"Enter {name}'s test score for {subject} (0 - 100): ")
                try:
                    score = int(score) #converting the score to int using type conversion
                    if 0 <= score <= 100:
                        subjects[subject] = score #store the subject and score
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Please enter the score as a whole number between 0 and 100.")
        students[name] = subjects #add the student to the main dictionary

    elif option == 2: 
        if not students: #using if not operator to check for empty dictionary
            print("Sorry, no student data has been entered.")
        else:
            print("+=+=+=+Summary Report+=+=+=")
            for name, subjects in students.items():
                scores = list(subjects. values()) #get all scores for the student
                average = round(sum(scores) / len(scores), 2) #calculating the average score
                #concatenating subjects and scores 
                subject_scores = ', '.join(f"{sub}:{score}" for sub, score in subjects.items())
                print(f"{name}'s scores: {subject_scores} | Average Score: {average}")

    elif option == 3:
        print("+=+=+=+Student Search+=+=+=+")
        name = input("Enter a student name to search: ")
        if name in students: #checking if the entered name exxists in the student dictionary
            subjects = students[name] #getting the subjects and scores for the student
            scores = list(subjects.values()) 
            average = round(sum(scores) / len(scores), 2) #calculating the average score
             #concatenating subjects and scores 
            subject_scores = ', '.join(f"{sub}:{score}" for sub, score in subjects.items())
            print(f"{name}'s scores: {subject_scores} | Average Score: {average}")
        else:
            print("Student not found.")
            
    elif option == 4:
        print("The Gradebook Manager is exiting. Goodbye!")
        break #exiting out of the loop
        
  


        
        

            
            
        
    
            
            
               
