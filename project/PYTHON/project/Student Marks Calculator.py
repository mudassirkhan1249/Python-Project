# Student Marks Calculator
import csv

# Student Marks Calculatorno
def invalidation(a):
    if len(a) > 16:
        print("Name is too long. Please enter a valid name.")
        print("Enter 1 to restart the program: ")
        restartInput()
        return

# Function to handle restart input
def restartInput():
    while True:
        inp = input("____:")
        if inp == "1":
            student_marks_calculator()
            break
        else:
            print("Invalid input. You can only enter 1 to restart the program.")

# Main function       
def student_marks_calculator():
    # Main function to calculate student marks, percentage, and grade
    try:
        name = str(input("Enter Student Name: "))
        if not name.replace(" ", "").isalpha():
            print("Invalid name entered. Please enter a valid name.")
            print("Enter 1 to restart the program: ")
            restartInput()
            return
        if name.isnumeric():
            print("Invalid name entered. Please enter a valid name.")
            print("Enter 1 to restart the program: ")
            restartInput()
            return
        if len(name) < 2:
            print("Name is too short. Please enter a valid name.")
            print("Enter 1 to restart the program: ")
            restartInput()
            return
        invalidation(name)
        numOfSub = int(input("Enter number of subjects i.e.(6): "))
        if numOfSub <= 0:
            print("Invalid number of subjects. Please enter a positive integer.")
            print("Enter 1 to restart the program: ")
            restartInput()
            return
        if numOfSub > 20:
            print("Too many subjects. Please enter a number less than or equal to 20.")
            print("Enter 1 to restart the program: ")
            restartInput()
            return
        marksOfEachSub = list(numOfSub * [0])

        for i in range(numOfSub):
            marksOfEachSub[i] = int(input(f"Enter marks of subject {i+1}: "))
            if marksOfEachSub[i] < 0 or marksOfEachSub[i] > 100:
                print("Invalid marks entered. Please enter marks between 0 and 100.")
                print("Enter 1 to restart the program: ")
                restartInput()
                return

        totalMarks = sum(marksOfEachSub)
        percentage = (totalMarks / (numOfSub * 100)) * 100

        grade = ''

        if percentage >= 90:
            grade = 'A+'    
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B+'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        elif percentage >= 40:
            grade = 'D'
        else:
            grade = 'F'
    
        print(f"Student Name: {name}")
        print(f"Total Marks: {totalMarks}")
        print(f"Percentage: {round(percentage ,2)}%")
        print(f"Grade: {grade}")
        print(f"Number of Subjects: {numOfSub}")

        # Save to CSV
        import os

        def dataSave():
            file_exists = os.path.exists('students_records.csv')
            with open('students_records.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:  # agar file pehli dafa ban rahi hai
                    writer.writerow(["Name", "Total Marks", "Percentage", "Grade", "Number of Subjects"])
                writer.writerow([name, totalMarks, round(percentage ,2), grade, numOfSub])
            print("Data saved to students_records.csv")
        dataSave()
        # Save to TXT
        print("Do you want to save the result to a txt file? (yes/no): ")
        saveToFile = input("____: ").strip().lower()
        if saveToFile == 'yes' or saveToFile == 'Yes' or saveToFile == 'YES':
            with open(f"{name}_marks.txt", "w") as file:
                file.write(f"Student Name: {name}\n")
                file.write(f"Total Marks: {totalMarks}\n")
                file.write(f"Percentage: {round(percentage ,2)}%\n")
                file.write(f"Grade: {grade}\n")
                file.write(f"Number of Subjects: {numOfSub}\n")
            print(f"Result saved to {name}_marks.txt")
        elif saveToFile == 'no' or saveToFile == 'No' or saveToFile == 'NO':
            print("Result not saved.")
        else:
            print("Invalid input. Result not saved.")

        # Read all records
        def readRecords():
            with open('students_records.csv', mode='r') as file:
                reader = csv .reader(file)
                for row in reader:
                    print("{:<15} {:<12} {:<12} {:<8} {:<5}".format(row[0], row[1], row[2], row[3], row[4]))
        userInput = input("Do you want to read all student records? (yes/no): ").strip().lower()
        if userInput == 'yes' or userInput == 'Yes' or userInput == 'YES':
            readRecords()
        elif userInput == 'no' or userInput == 'No' or userInput == 'NO':
            print("Okay, not reading records.")
        else:
            print("Invalid input. Not reading records.")

        # End of program
        print("Enter 1 to restart the program: ")
        restartInput()
        return
    
    # Catch any unexpected errors
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Enter 1 to restart the program: ")
        restartInput()
        return

student_marks_calculator()