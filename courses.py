from user import User
import re


class Course(User):
    """A class to represent courses"""

    def __init__(self):
        """Initialization for course attributes"""
        super().__init__()

    def add_course(self, student_id : int, course : str):
        """Add course"""
        for student in self.record:
            if student_id == student["Student ID"]:
                if "," not in course:
                    student["Course"][course] = "N/A"
                else:
                    temp_list = course.split(",")
                    for course in temp_list:
                        student["Course"][course] = "N/A"

    def update_course(self, student_id : int, old_course : str, new_course : str):
        """Update Courses"""
        for student in self.record:
            if student_id == student["Student ID"]:
                student["Course"][new_course] = student["Course"].pop(old_course)

    def delete_course(self, student_id : int, course : str):
        """Delete Courses""";
        for student in self.record:
            if student_id == student["Student ID"]:
                del student["Course"][course]

    def view_course(self, student_id : int, course : str):
        """View Course"""
        for student in self.record:
            if student_id == student["Student ID"]:
                output = student["Course"][course]
                return output

    def list_course(self, student_id : int):
        """List All Courses"""
        output = "Course - Grade\n"
        for student in self.record:
            if student_id == student["Student ID"]:
                for key,value in student["Course"].items():
                    output += f"{key} - {value}\n"
                return output




