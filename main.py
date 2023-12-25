import os

# File to store student information
db_file = "student_database.txt"

#creates file if there is no existing one
if not os.path.exists(db_file):
    with open(db_file, "w") as file:
        pass

# Function to perform insertion sort on a list
def insertion_sort(lst, key=lambda x: x):
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1
        while j >= 0 and key(current) < key(lst[j]):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current

# Function to handle different menu options
#Condition if the user chooses '1' from the main menu
def optionsConditions(MenuOptions):
    if MenuOptions == '1':
        os.system('cls')
        print("  You choose option [1] ADD STUDENT")
        print("____________________________________\n")
        print("Type 'exit' to go back to the main menu\n\n")
        while True:
            full_name = input("Enter student's First name: ")
            
            #breaks the loop if the user types 'exit' and goes back to main menu  
            if full_name.lower() == 'exit':
                break
            
            # Split the full name into a list of words
            name_parts = full_name.split()
            
            # Ensure there is at least one part (first name)
            if len(name_parts) >= 1:
                first_name = ' '.join(name_parts)  # Join all parts for the first name
                last_name = input("Enter student's Last Name: ")
            else:
                print("Invalid input. Please enter at least a first name.")
                continue
            
            #stores the user input to the created file 
            with open(db_file, "a") as file:
                file.write(f"{first_name},{last_name}\n")
            os.system('cls')
            print("____________________________________\n")
            print("Type 'exit' to go back to the main menu\n")
            print(f"You have added '{first_name} {last_name}'.\n\n")

    #Condition if the user chooses '2' from the main menu
    elif MenuOptions == '2':
        os.system('cls')     
        print("  You choose option [2] SEARCH NAME OF STUDENT")
        print("_____________________________________________")
        print("Type 'exit' to go back to the main menu\n\n")
        
        #the loop will continue if the user do not type 'exit'
        while True:
            found = False
            
            #opens the file and then read through the lines to search the inputted name
            search_name = input("Search Student: ")
            with open(db_file, "r") as file:
                lines = file.readlines()
                insertion_sort(lines, key=lambda x: x.strip().split(',')[1].strip().lower())
                
                #displays the found name to the screen
                for line in lines:
                    first_name, last_name = line.strip().split(',')
                    full_name = f"{first_name} {last_name}"
                    if full_name.lower() == search_name.lower():
                        found = True
                        os.system('cls') 
                        print("Student found:\n")
                        print("Name:", full_name)
                        print("_______________________________________________\n\n")
            
            #displays a message if the inputted name is not found           
            if not found:          
                os.system('cls')          
                print("Student", search_name, "not found\n")
                print("_______________________________________________\n\n")
            
            #breaks the loop if the user types 'exit' and goes back to main menu             
            if search_name.lower() == 'exit':
                break
    
    #Condition if the user chooses '3' from the main menu
    elif MenuOptions == '3':
        os.system('cls')
        print("  You choose option [3] DISPLAY LIST OF STUDENTS")
        print("_______________________________________________")
        print()
        
        #opens the file and read through the lines and then using the insertion_sort() function to sort the names
        with open(db_file, "r") as file:
            lines = file.readlines()
            insertion_sort(lines, key=lambda x: x.strip().split(',')[1].strip().lower())
            
            #prints the list of students in the screen
            print("                  STUDENT LIST")
            print("         _____________________________")
            print()
            for line in lines:
                first_name, last_name = line.strip().split(',')
                print(f"Name: {first_name} {last_name}")

        #breaks the loop if the user types 'exit' and goes back to main menu 
        print("\n\n[exit] Exit")
        displayStudent = input("Enter key option: ")
    
        if displayStudent.lower() == 'exit':
            return

    #Condition if the user chooses '4' from the main menu
    elif MenuOptions == '4':
        os.system('cls')
        print("     You choose option [4] REMOVE STUDENT")
        print("_____________________________________________\n")
        print("Type 'exit' to go back to the main menu\n\n")
        
        #continues to run the loop if the user do not type 'exit'
        while True:
            removed = False
            removeStudent = input("Enter the Full Name of Student to Remove (First Last): ")

            if removeStudent.lower() == 'exit':
                break
            
            #opens the file and search through the lines to find the inputted name from the user
            with open(db_file, "r") as file:
                lines = file.readlines()

            #modifies and updates the file removing the inputted name from the user
            with open(db_file, "w") as file:
                insertion_sort(lines, key=lambda x: x.strip().split(',')[1].strip().lower())
                for line in lines:
                    first_name, last_name = line.strip().split(',')
                    full_name = f"{first_name} {last_name}"
                    if full_name.lower() == removeStudent.lower():
                        removed = True
                        os.system('cls')
                        print(f"{removeStudent} has been removed successfully!")
                        print("_____________________________________________\n\n")
                    else:
                        file.write(f"{first_name},{last_name}\n")

            #prints a message if the inputted text is not found in the file
            if not removed:
                os.system('cls')
                print(f"{removeStudent} not found. No student removed.\n")
                print("_____________________________________________\n\n")
                
    #Condition if the user chooses '5' from the main menu
    elif MenuOptions == '5':
        os.system('cls')
        print("     You choose option [5] EDIT STUDENT NAME")
        print("_____________________________________________\n")
        print("Type 'exit' to go back to the main menu\n\n")
        
        #continues to run the code if the user do not type 'exit'
        while True:
            edited = False
            old_name = input("Enter the Full Name of Student to Edit (First Last): ")

            if old_name.lower() == 'exit':
                break
            
            #opens the file and read through the lines to find the inputted name from the user
            with open(db_file, "r") as file:
                lines = file.readlines()
                
            #modifies and updates the file with the edited name that was inputted by the user
            with open(db_file, "w") as file:
                
                #using insertion sort to sort the names
                insertion_sort(lines, key=lambda x: x.strip().split(',')[1].strip().lower())
                for line in lines:
                    first_name, last_name = line.strip().split(',')
                    full_name = f"{first_name} {last_name}"
                    if full_name.lower() == old_name.lower():
                        edited = True
                        new_name = input("Enter the New First Name: ")
                        # Split the full name into a list of words
                        name_parts = new_name.split()
                        
                        # Ensure there is at least one part (first name)
                        if len(name_parts) >= 1:
                            first_name = ' '.join(name_parts)  # Join all parts for the first name
                            last_name = input("Enter the New Last Name: ")
                            new_name = f"{first_name} {last_name}"
                            file.write(f"{first_name},{last_name}\n")
                            print(f"\n{old_name} has been edited to {new_name} successfully!")
                            print("_____________________________________________\n\n")
                        else:
                            print("Invalid input. Please enter at least a first name.")
                            continue
                    else:
                        file.write(f"{first_name},{last_name}\n")

            #prints a message if the inputted name is not found in the file
            if not edited:
                print(f"\n\n{old_name} not found. No student edited.\n")
                print("_____________________________________________\n\n")


    #This is the main menu options. It prompts the user to enter a valid key option
    while True:
        os.system('cls')
        print("WELCOME TO MAIN MENU\n")
        print("[1] Add Student")
        print("[2] Search Name of Student")
        print("[3] Display List of Students")
        print("[4] Remove Student")
        print("[5] Edit Student Name")
        print("[6] Exit")
        MenuOptions = input("Enter key option: ")
        os.system('cls')
        
        if MenuOptions == '6':
            os.system('cls')
            print("_____________________________________________\n")
            print("\nSuccessfully exited the program. Thank you for using our system!\n")
            print("\n_____________________________________________")
            exit(0)

        #calling the optionsConditions() function to handle different key options
        optionsConditions(MenuOptions)

# Call the main loop if the user entered a wrong key option
optionsConditions('0')  # Initialize the loop with a dummy option

