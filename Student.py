from User import User

class Student(User):


    def __init__(self, dni: str, firstName: str, lastName:str, email:str, username:str, tipo:str, following, admin,major):
        self.major = major
        super().__init__(dni, firstName, lastName, email, username,tipo, following, admin)
        

