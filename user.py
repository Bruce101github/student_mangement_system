from student import Student
import random

class User(Student):
    """A class to represent a user in the student management system"""

    def __init__(self):
        super().__init__()
        """Initialize the attributes of a user"""
        self.admin = [{
                        "First Name" : "Bruce",
                        "Last Name" : "Thiombiano",
                        "Username" : "bruce101",
                        "Password" : "Test123!?",
                        },]  # List to store admin-related information or actions

    def add_student(self):
        """Add a new student to the record"""
        # Gather student information from user input
        first_name = input("Enter Student's First name: ")
        last_name = input("Enter Student's Last name: ")
        age = input("Enter Student's age: ")
        gender = input("Male/Female: ")
        courses = input("Enter Courses: ")
        courses = courses.split(",")  # Split the input courses into a list

        # Add student information to the record
        self.record.append({
            "Student ID": None,  # Placeholder for student ID to be assigned later
            "First Name": first_name,
            "Last Name": last_name,
            "Age": age,
            "Gender": gender,
            "Course": {}  # Dictionary to hold course names and their values
        })
        
        # Add courses to the student's record
        for course in courses:
            self.record[-1]["Course"][course.title()] = 0
        
        # Assign a unique Student ID
        while True:
            unique = True
            assigned_id = random.randrange(9999, 99999)  # Generate a random ID
            for student in self.record:
                if student["Student ID"] == assigned_id:
                    unique = False  # ID is not unique, generate a new one
            if unique:
                self.record[-1]["Student ID"] = assigned_id
                break  # Exit loop once a unique ID is found
        
        return f"Student successfully added. Student ID {self.record[-1]['Student ID']}"

    def update_student(self, student_ID: str, key: str, value: str):
        """Update details of an existing student"""
        for student in self.record:
            if student["Student ID"] == student_ID:
                student[key] = value  # Update the specific detail of the student

    def delete_student(self, student_ID):
        """Delete a student's record"""
        for student in self.record:
            if student["Student ID"] == student_ID:
                self.record.remove(student)  # Remove student from the record
                return f"Student with ID {student_ID} successfully deleted."

    def view_student(self, student_id):
        """View details of a specific student"""
        output = ""
        for student in self.record:
            if student["Student ID"] == student_id:
                output += f"Name: {student['First Name']} {student['Last Name']}\n"
                output += f"Age: {student['Age']} years.\n"
                output += f"Gender: {student['Gender']}\n"
                output += f"Courses: {', '.join(student['Course'])}\n"  # List all courses
        return output

    def list_student(self):
        """List details of all students"""
        output = ""
        for student in self.record:
            output += f"Name: {student['First Name']} {student['Last Name']}\n"
            output += f"Age: {student['Age']} years.\n"
            output += f"Gender: {student['Gender']}\n"
            output += f"Courses: {', '.join(student['Course'])}\n"  # List all courses
            output += "-" * 30 + "\n"  # Separator between student records
        return output

