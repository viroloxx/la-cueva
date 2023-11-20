

class User:


    def __init__(self, dni: str, firstName: str, lastName:str, email:str, username:str, tipo:str, following, admin):
        self.dni = dni
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.tipo = tipo   
        self.following = following
        self.admin = admin
        self.posts = []
        self.comments= []
        self.infracciones = 0



#------------------IMPRIMIR LOS DATOS-----------------------------------------------------
    def get_all_user(self):
        return f"""
        Nombre: {self.name} 
        Apellido: {self.lastName}
        Usuario: {self.username} 
        Email: {self.email}
        
        
        """


    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_user(self):
        return self.user

    def get_email(self):
        return self.email

#-----------------------ESTABLECER NUEVA DATA-------------------------------------------------
    def set_name(self):
        self.name = new_name
    
    def set_last_name(self):
        self.last_name = new_last_name

    def set_username(self):
        self.user = new_user
    
    def set_mail(self):
        self.mail = new_mail

    def set_carreer(self):
        self.carreer = new_carreer



        
   #-----------------------FOLLOW------------------------------






   # -------------------  
def follow_user(self, user):
    if self.department == user.department:
        self.following.append(user)
    
    
    luser = input("ingrese el usuario que esta buscando ")
    for user in users:


        if user_active.department == userB.department:
            userA.following.append(userB.id)
        else: 
            userB.pendingFollows.append(userA.id)

        
def search_username(self, username, department):
    
    s_users = []
    d_users = []
    search_u = input("""
                BUSQUEDA

        Bienvenido a su buscador, donde podra ver a sus amigos y profesores
        
        1. Busqueda por Usuario
        2. En caso de no conocerlo, seleccione el departamento del que desea buscar.
        3. Revisar el perfil de Usuario que busco.
        0. Vuelta al menu.
    """)
    while search_u != 1 and search_u != 2 and search_u != 3:
        if search_u == 1:
            s_u = input("Ingrese al usuario que desea buscar: ")
            while s_u not in self.users: 
                s_u = input(f"Error!!, {s_u} no existe, vuelve a intentarlo")
            for user in users:
                for k, v in user.items():
                    if k == username:
                        s_users.append(k)
            print(s_users)
            print("selecione 0 para volver al menu")

        elif search_u == 2:
            
            s_d = input("Ingrese al usuario que desea buscar: ")
            while s_u not in Api.departments:
                for user in users:
                    if user.department == department:
                        d_users.append(user)

            print(d_users)
            print("selecione 0 para volver al menu")


                
            self.user_active.append(login_in_user)
            menu(self)
            

    def access_user(self, Username, Post):
        print(f"Name: {s_users.get_name()}")
        print(f"Username: {s_users.get_username()}")
        a_posts = s_users.get_posts()
        print("lista de post")
        for post in a_posts:
            print(post)

        p_id = input("introduzca el id del post: ")
        s_users.get_posts(p_id)


        
