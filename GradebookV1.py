#this program is version 1 of a student gradebook manager

students = {} #storing the student details in a dictionary
while True:
    #displaying the menu options
    print("+=+=+=+=+=+Student Gradebook Manager+=+=+=+=+=+")
    print("1. Add a student")
    print("2. Display all students")
    print("3. Search for a student")
    print("4. Exit")
    option = input("Please choose an option (1-4): ")
    if option == "1":
        #asking for user details
        name = input("Enter the student's name: ")
        subjects = {} #storing the students subjects and scores in a dictionary
        while True:
            subject = input(f"Enter the subject for {name}. Type 'done' to finish: ")
            if subject.lower() == "done": #exiting the while loop once "done" has been entered
                break
            score = input(f"Enter {name}'s test score for {subject}: ")
            try:
                score = float(score) #converting the score to float using type conversion
                
            except ValueError:
                print("Please enter the score as an integer.")
        print(f"{name}'s details have been saved. Thank you!")

        
