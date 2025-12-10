# Task 1: Dictionary of Student Marks with user input

student_marks = {}

# How many students you want to enter?


while True:
    n = input("How many students? ")

# Check if input is interger or not

    if n.isdigit():
        n = int(n)

# Take name and marks as input and store in dictionary

        for i in range(n):
            name = input("Enter student name: ")
            marks = int(input(f"Enter {name}'s marks: "))
            student_marks[name] = marks

# Ask for a name to search

        search_name = input("Enter the student name to search marks: ")

# Display result

        if search_name in student_marks:
            print(f"Marks of {search_name} = {student_marks[search_name]}")

        else:
            print("Student not found in record.")
        break
    else:
        print("Invalide character! only integers are allowed.")