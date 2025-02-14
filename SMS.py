# Student record management system
students = {}    # to store the student data
students_id = {}   # list to track the student id's(data)

while True:
    print("/n1.Add the student record")
    print("2.View all students")
    print("3.Searching all the students")
    print("4.Update the students data")
    print("5.Delete the student data")
    print("6.exit")

    choice = input("enter your choice")

    if choice == '1':
        students_id = input("Enter a student id")
        name = input("Enter the name of student")
        age = input("Add the age of student")
        grade = input("Enter the grade of students")
        students[students_id] = {'name': name, 'age': age, 'grade': grade}
        students_id.append(students_id)
        print("Students data get added succesfully")

    elif choice == '2':
        if not students:
            print("No data found")
        else:
            for students_id in students_id:
                student = students[students_id]
                print(f"ID: {students_id}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    elif choice == '3':
        students_id = input("Enter a student id to search")
        if students_id in students:
            student = students[students_id]
            print(f"ID: {students_id}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        else:
            print("Students not found")

    elif choice == '4':
        students_id = input("Enter student id to update")
        if students_id in students:
            name = input("Enter a new name :")
            age = input("Enter a new age :")
            grade = input("Enter a new grade :")
            students[students_id] = {'name': name, 'Age': age, 'Grade': grade}
            print("Student information updated succesfully")
        else:
            print("students not found")
    
    elif choice == '5': 
        student_id = input("Enter student ID to delete: ")
        if student_id in students:
            del students[student_id]
            student_ids.remove(student_id)
            print("Student record deleted successfully!")
        else:
            print("Student not found.")
            
    elif choice == '6':  
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please try again.")