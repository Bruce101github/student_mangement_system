from grade import Grade
from authentication import Auth
import time

def main():
    authy = Auth()
    admin = Grade()
    username = input("Enter username: ")
    password = input("Enter password: ")
    valid = authy.authentication(username,password)

    if valid:
        for i in range(1,101):
            print(f"loging in...{str(i)}%", end="\r")
            time.sleep(0.01)
    else:
        print("Login failed")
      
    while valid == True:
        command = input("Enter command: ")
        if command.lower() == "q":
            break
        elif command.lower() == "add student":
            print(admin.add_student())
        elif command.lower() == "update student":
            student_ID = int(input("Enter Student ID: "))
            key = input("Enter info you want to update: ")
            value = input("Enter new value")
            admin.update_student(student_ID,key,value)
            print("Update Successful")
        elif command.lower() == "delete student":
            student_id = int(input("Enter Student ID: "))
            print(admin.delete_student(student_id))
        elif command.lower() == "view student":
            student_id = int(input("Enter Student ID: "))
            print(admin.view_student(student_id))
        elif command.lower() == "list student":
            print(admin.list_student())
        elif command.lower() == "add course":
            student_id = int(input("Enter Student ID: "))
            course = input("Enter course: ")
            admin.add_course(student_id, course)
            print("Course successfully added")
        elif command.lower() == "update course":
            student_id = int(input("Enter Student ID: "))
            old_course = input("Enter old course: ")
            new_course = input("Enter new course: ")
            admin.update_course(student_id, old_course, new_course)
            print("Course successfully updated")
        elif command.lower() == "delete course":
            student_id = int(input("Enter Student ID: "))
            course = input("Enter course: ")
            confirm = input(f"Are you sure you want to delete {course.title()}.yes/no ")
            if confirm.lower() == "yes":
                admin.delete_course(student_id, course)
                print(f"{course.title()} has been successfully delete.")
        elif command.lower() == "view course":
            student_id = int(input("Enter Student ID: "))
            course = input("Enter course: ")
            print(admin.view_course(student_id, course))
        elif command.lower() == "list course":
            student_id = int(input("Enter Student ID: "))
            print(admin.list_course(student_id))
        elif command.lower() == "add grade":
            student_id = int(input("Enter Student ID: "))
            course = input("Enter course: ")
            grade = input("Enter grade: ")
            admin.add_grade(student_id, course, grade)
            print(f"{course.title()} has been successfully graded.")
        elif command.lower() == "view grade":
            student_id = int(input("Enter Student ID: "))
            course = input("Enter course: ")
            print(admin.view_grade(student_id, course))
        elif command.lower() == "list grade":
            student_id = int(input("Enter Student ID: "))
            print(admin.list_grade(student_id))




if __name__ == "__main__":
    main()

        
