from student import Student
import student_crud


def main():
    while True:
        print("\n===== Student Progress Tracker =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")
        print("6. Export Student Data to PDF")


        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            course = input("Enter course: ")
            marks = int(input("Enter marks: "))
            attendance = int(input("Enter attendance (%): "))
            remarks = input("Enter remarks: ")
            student = Student(name, roll, course, marks, attendance, remarks)
            student_crud.add_student(student)

        elif choice == "2":
            student_crud.view_students()

        elif choice == "3":
            roll = input("Enter roll number to update marks: ")
            new_marks = int(input("Enter new marks: "))
            student_crud.update_marks(roll, new_marks)

        elif choice == "4":
            roll = input("Enter roll number to delete: ")
            student_crud.delete_student(roll)

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            student_crud.export_to_pdf()



        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
