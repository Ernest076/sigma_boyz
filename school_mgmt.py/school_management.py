import pandas as cd
 # Step 1: Create an empty list to store student records
students = []

#Step 2: Function to register new students
def register_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Current Course: ")
    phone_number = input("Enter Phone Number")

    student = {
        "ID" : student_id,
        "Name" : name,
        "Course" : course,
        "Phone number" : phone_number,
        "Grade": None,
        "New Course": None
    }
    
    students.append(student)
    print(f"Student {name} registered successfully!\n")

# Step 3: Assign new courses based on grades
def assign_courses():
    if not students:
        print(f"No students to assign courses.\n")
        return
    for s in students:
        grade = input(f"Enter grade for {s['Name']} (A/B/C/D/E): ")
        s["Grade"] = grade
        if grade == "A":
            s["New Course"] = "Advanced Studies"
        elif grade == "B":
            s["New Course"] = "Intermediate Studiies"
        elif grade == "C":
            s["New Course"] = "General Studies"
        elif grade == "D":
            s["New Course"] = "Remedial Studies"
        elif grade == "E":
            s["New Course"] = "Repeat Course"
    print(f"Courses assigned based on grades!\n")


# Step 4: Data saving to Excel
def menu():
    while True:
        print("1. Register Student")
        print("2. Display Students")
        print("3. Assign Course")
        print("4. Save to Excel")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
           def display_students():
               # Code to display students goes here
               pass # Placeholder if function body is empty for now
        elif choice == "3":
            assign_courses()
        elif choice == "4":
           def save_to_excel():
               # Code to save to excel goes here
               pass # Placeholder if function body is empty for now
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

#Run the program
menu()


import pandas as pd

def save_to_excel(students):
    #Convert list of dictionaries into a DataFrame
    df = pd.DataFrame(students)

    #Save to Excel file
    df.to_excel("school_mgmt.xlsx", index = False)

    print("Student data saved to school_mgmt.xlsx")


    save_to_excel( students)
    
    students = [
        {"ID":"1342526", "Name":"Alyssa", "Course":"Interior Design", "Phone":"0786433627", "Grade":"A", "New Course":"Mechatronics"},
{"ID":"23638399", "Name":"Barthold", "Course":"Law", "Phone":"0786234361", "Grade":"B", "New Course":"Automotive Engineering"}
    ]
    
    save_to_excel(students)
