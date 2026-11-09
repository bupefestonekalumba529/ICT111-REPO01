# Define grade scale
A = range(80, 101) # Excellent
B = range(70, 80) # Very Good
C = range(60, 70) # Good
D = range(50, 60) # Pass
F = range(0, 50) # Fail

print(" [**Welcome to the Student Grading System**] " )
print("1. Add student") # Allows the user to add a student and their academic details, including student number, name, course, mark, grade and decision.
print("2. Display all") # Displays the details of all students
print("3. Class summary") # Displays the total number of students, total passed, total failed, highest mark, lowest mark and average mark.
print("4. Exit") # Exits the program.

students = [] # students is a list that stores the dictionaries of students, where each dictionary contains the academic details of a student.
while True:
    choice = input("Enter your choice : ")
    if choice == "1": # Add students
        student_number = input("Enter student number : ") 
        name = input("Enter student name : ")                                                                                                                                                                                                                                                                                                                                                                                                                             
        course = input("Enter student course : ")
        mark = float(input("Enter student mark : "))
        if mark < 0 or mark > 100: # Only numbers between 0 and 100 are accepted, and the program will prompt the user to enter a valid mark if the input is invalid.
            print("[Invalid mark!! Enter a mark between 0 and 100.]")
        elif mark != float(int(mark)): # Only whole numbers and decimal numbers are accepted, and the program will prompt the user to enter a valid mark if the input is invalid.
            print("[Invalid mark!! Enter a number between 0 and 100.]")
            continue # If the mark is invalid, the program will prompt the user to enter a valid mark and continue to the next iteration of the loop without adding the student.
        student = {"student_number": student_number, "name": name, "course": course, "mark": mark} # student is a dictionary that stores the academic details of students in the list of students.
        if mark in A:
            grade = "A"
            decision = "EXCELLENT"    
        elif mark in B:
            grade = "B"
            decision = "VERY GOOD"    
        elif mark in C:
            grade = "C"
            decision = "GOOD"    
        elif mark in D:
            grade = "D"
            decision = "PASS"    
        elif mark in F:
            grade = "F"
            decision = "FAIL"
        student.update({"grade": grade, "decision": decision})
        students.append(student)
    elif choice == "2": # Display all students
        print(" [***Student Reports***] ")
        for student in students:
                print(student)

    elif choice == "3": # Class summary
        print(" [***Class summary***] ")
        print(f"Total students: {len(students)}")
        print(f"Total passed: {len([s for s in students if s['decision'] != 'FAIL'])}")
        print(f"Total failed: {len([s for s in students if s['decision'] == 'FAIL'])}")
        print(f"Highest mark: {max(s['mark'] for s in students)}") # The highest mark is calculated by using the max() function, it extracts the 'mark' value from each student dictionary in the list of students and finds the maximum mark among all students.
        print(f"Lowest mark: {min(s['mark'] for s in students)}") # The lowest mark is calculated by using the min() function, it extracts the 'mark' value from each student dictionary in the list of students and finds the minimum mark among all students.
        print(f"Average mark: {sum(s['mark'] for s in students) / len(students)}")
    elif choice == "4": # Exit
        print("[**Exiting the program...**]")
        break
    else:
        print("[Invalid choice!! Enter another choice.]")