from User import User

class Professor(User):

    def __init__(self, dni: str, firstName: str, lastName:str, email:str, username:str, tipo:str, following, admin, department):
        self.department = department    
        super().__init__(dni, firstName, lastName, email, username, tipo, following, admin)
        

