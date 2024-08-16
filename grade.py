from courses import Course
import re


class Grade(Course):
    """A class to represent the course grades."""

    def __init__(self):
        super().__init__()
        """Initialize the attributes"""

    def add_grade(self, student_id : int, course : str, grade : str):
        """Add grade"""
        for student in self.record:
            if student_id == student["Student ID"]:
                for courses in student["Course"]:
                    if courses["Title"] == course.title():
                        courses["Grade"] = grade
        super().save(self.record)


    def view_grade(self, student_id : int, course : str):
        """View grade"""
        for student in self.record:
            if student_id == student["Student ID"]:
                for courses in student["Course"]:
                    if courses["Title"] == course:
                        output= f"{courses["Title"]} - {courses["Grade"]}"
        return output
    
    def list_grade(self, student_id : int):
        """List grade"""
        output = "\nCourse - Grade"
        for student in self.record:
            if student_id == student["Student ID"]:
                for courses in student["Course"]:
                    output += f"\n{courses["Title"]} - {courses["Grade"]}"
        return output



















