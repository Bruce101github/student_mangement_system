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
                     self.record[-1]["Course"].append({
                                        "Title" : course.title(),
                                        "Description" : "N/A",
                                        "Ojectives" : [],
                                        "Instructior" : "N/A",
                                        "Credits" : "N/A",
                                        "Grade" : "N/A",
                                        })
                else:
                    temp_list = course.split(",")
                    for course in temp_list:
                         self.record[-1]["Course"].append({
                                        "Title" : course.title(),
                                        "Description" : "N/A",
                                        "Ojectives" : [],
                                        "Instructior" : "N/A",
                                        "Credits" : "N/A",
                                        "Grade" : "N/A",
                                        })


    def update_course(self, student_id : int, old_course : str, new_course : str):
        """Update Courses"""
        for student in self.record:
            if student_id == student["Student ID"]:
                for course in student["Course"]:
                    if course["Title"] == old_course:
                        course["Title"] = new_course

    def delete_course(self, student_id : int, course : str):
        """Delete Courses""";
        for student in self.record:
            if student_id == student["Student ID"]:
                for courses in student["Course"]:
                    if courses["Title"] == course:
                        student["Course"].remove(courses)

    def view_course(self, student_id : int, course : str):
        """View Course"""
        output = ""
        for student in self.record:
            if student_id == student["Student ID"]:
                for courses in student["Course"]:
                    if courses["Title"] == course:
                        for key,value in courses.items():
                            output += f"{key} - {value}\n"
                return output

    def list_course(self, student_id : int):
        """List All Courses"""
        output = "-" * 30 + "\n"
        for student in self.record:
            if student_id == student["Student ID"]:
                for courses in student["Course"]:
                    for key,value in courses.items():
                        output += f"{key} - {value}\n"
                    output += "-" * 30 + "\n"
                return output




