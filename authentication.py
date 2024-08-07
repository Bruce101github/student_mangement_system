from user import User

class Auth(User):
    """A class to authenticate users in the student management system"""

    def __init__(self):
        super().__init__()
    
    def authentication(self, username : str, password : str):
        """Authenticate user credentials"""
        for user in self.admin:
            if (user["Username"] == username) and (user["Password"] == password):
                return True
            else:
                return False


