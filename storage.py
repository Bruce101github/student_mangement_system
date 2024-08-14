import json


class Storage():
    """A simple representations of a database"""

    def __init__(self, file : str = "database.json"):
        """Initialization"""
        self.file = file
        self.path = path(file)

    def save(self, record : list):
        """Saves data to the database"""
        content = json.dumps(record)
        self.path.write_text(content)

        
    def load(self):
        """Loads save data"""
        content = self.path.read_text()
        json.loads(content)
