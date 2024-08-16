from storage import Storage

class Student(Storage):
    """A class to represent a student in the student management system"""

    def __init__(self):
        super().__init__(file = "database.json")
        """Initialize student records"""
        self.record = []
   
 
