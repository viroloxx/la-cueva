from User import *
from Post import *
import Api
import random
import uuid
from Student import *
from Professor import *
from Admin import *
#Registro automatico al iniciar el programa si no existe informacion ya guardada
class Metrogram():
    def __int__(self, usernames = [], departments = [], posts = [], user_acti = []):
        usernames = usernames
        departments =  departments
        posts =  posts
        user_active = user_active
        comments = comments
    
    def welcome(self):
        usernames = []
        user_active = []
        posts = []
        departments = []
        comments = []
        user_post_c = {}
        department_post_c = {}

        Api.get_users(usernames)
        Api.get_posts(posts)
        while True:
            print("""
                Bienvenido a Metrogram

                Para ingresar debe seleccionar:
                1. Ingresar.
                2. Registarse.
                3. Salir
            """)
            option_0 = input("Seleccione: ")
            while option_0 != "1" and option_0 != "2" and option_0 != "3":
                option_0 = input("error, Seleccione una opcion valida: ")
            
            option_0 = int(option_0)
#aqui se hace un log in comparando los datos de la api
            if option_0 == 1:
                login_in_user = input("Ingrese usuario: ")
                users_w = []
                for i in usernames:
                    users_w.append(i.username.lower())
                while not login_in_user.lower() in users_w: 
                    for user in usernames:
                        login_in_user =input(f"Error!!, {login_in_user} no existe, vuelve a intentarlo")
                user_active.append(login_in_user)
                self.menu()
#aqui se crea un nuevo objeto, para despues agregarlo a la api                       
            elif option_0 == 2:
                dni = (uuid.uuid1()) 
                name = input("Ingrese su nombre:").capitalize()
                while not name.isalpha():
                    name = input("Error, Ingresa el nombre: ").capitalize()

                last_name = input("Ingrese su apellido:").capitalize()
                while not last_name.isalpha():
                    last_name = input("Error, Ingresa el nombre: ").capitalize()

                mail = input("Ingrese su correo, no olvide colocar (@correo.unimet.edu.ve):")
                while not mail.endswith("@correo.unimet.edu.ve"):
                    mail = input("Error, Ingresa de nuevo su correo: ")

                user = input("Ingrese su usuario:")
                while not user.isalpha():
                    user = input("Error, ingrese su usario")

                admin = input("usted es administrador(S/N): ")
                while not admin.isalpha():
                    admin = input("Error, usted es administrador(S/N): ") 
                if admin == "S":
                    admin = True
                else:
                    False

                following = []

                tipo = input("Ingrese si es estudiante (E) o profesor (P):").capitalize()

                while tipo != "E" and tipo != "P":
                    tipo = input("Error,Ingrese si es estudiante (E) o profesor (P):").capitalize()
                
                if tipo == "E":
                    tipo = "student"
                    major = input("Ingrese su carrera/departamento:").capitalize()
                    while not major.isalpha():
                        major = input("Error, Ingresa la carrera que esta cursando: ").capitalize()
                    user = Username(dni, name, last_name, mail, user, following, admin, tipo, major)
                    usernames.append(user)
                    user_active.append(user)
                    self.menu()
                    

                elif tipo == "P":
                    tipo = "professor"
                    department = input("Ingrese su departamento:").capitalize()
                    while not department.isalpha():
                        department = input("Error, Ingrese el departamento que pertenece: ").capitalize()
                    user = Username(dni, name, last_name, mail, user, following, admin, tipo, department)
                    usernames.append(user)
                    user_active.append(user)
                    self.menu()

            elif option_0 == 3:
                break

                
    def menu(self):
        while True:
            print("""
                    MENU
                ------------
                1. Gestion de Perfil.
                2. Gestion de Multimedia.
                3. Gestion de Interaccines.
                4. Gestion de Moderacion.
                5. Indicaciones.
                0. Salida.
            """)
            option_1 = input("Ingrese una opcion: ")
            while not int(option_1) in range(0,6):     
                option_1 = input("Error!!!, Ingrese una opcion: ")  

            option_1 = int(option_1) 
            
            if option_1 == 1:
                self.g_perfil()
                

            elif option_1 == 2:
                print("""
                    GESTION DE MULTIMEDIA
                ------------
                1. Hacer post.
                2. Ver likes de amigos.
                3. Buscador de posts.
                0. Menu.
                """)
                option_p = int(input("Ingrese su opcion:"))
                while option_p != 1 and option_p != 2 and option_p != 3 and option_p != 4:
                    option_p = input("Error, ingrese su opcion: ")
                    
                if option_p == 1:
                    publisher = user_active.username
                    tipo = input("Ingrese si es una foto (F) o video (V):") 
                    while  tipo != "F" and tipo != "V":
                            tipo= input("Error, Ingrese si es una foto (F) o video (V): ") 
                    if tipo == "F":
                        tipo = "photo"
                    elif tipo == "V":
                        tipo = "video"
                    caption = input("Ingrese la descripcion deseada: ").capitalize()
                    while not caption.isalpha():
                        caption = input("Error, Ingrese una descripcion: ")
                    date = input("Ingrese la fecha de publicacion (DD/MM/YYYY): ")
                    while not re.match(r"\d{2}/\d{2}/\d{4}", date):
                        date = input("Error, Ingresa de nuevo su correo: ")
                    tags = []
                    post = Post(puplisher, multimedia, caption, date, tags)
            
                    posts.append(post)
                    print(post.show_post())
                    break
                elif option_p == 2:
                    self.view_posts()
                elif option_p == 3:
                    self.search_posts
                elif option_p == 4:
                    break
                    Menu()
            elif option_1 == 3:
                print("""
                        GESTION DE INTERACCIONES
                    ------------
                    1. Seguimiento.
                    2. Deseguir.
                    3. Comentar.
                    4. Cambio de sesion.
                    5. Eliminar comentario.
                    6. Acceder al perfil.
                    0. Menu
                """)
                selection_user_b = input("Seleccione usuario que desea interactuar: ")
                
                user_b = []
                userb_active = []
                for i in usernames:
                    user_b.append(i.username.lower())
                while not selection_user_b.lower() in user_b: 
                    for user in usernames:
                        selection_user_b =input(f"Error!!, {selection_user_b} no existe, vuelve a intentarlo")
                userb_active.append(userb_active)
                
                option_i = input("seleccione una opcion: ") 
                while option_i != "1" and option_i != "2" and option_i != "3" and option_3 != "4" and option_3 != "5" and option_3 != "6" and option_3 != "7":
                    option_i = input("seleccione una opcion: ") 
               
                if option_i == 1:
                    e = input("ingrese usuario que quiere seguir: ")
                    for user in Post.publisher:
                        if e == user:
                            user_found.append(user)
                
                if option_i == 2:
                    pass
                if option_i == 3:
                    pass
                if option_i == 4:
                    pass
                if option_i == 5:
                    pass
                if option_i == 6:
                    pass

    #aqui mediante el atributo de admin colocado al user, se puede ingresar a esta seccion del menu
            elif option_1 == 4:
                if user_active.admin: 
                    option_adm = int(input("""
                             Menu de Moderacion

                        1. Eliminar un post que considere ofensivo:
                        2. Eliminar un comentario ofensivo:
                        3. Eliminar un usuario que infringido multiples veces las reglas:
                    
                    Introduzca al opcion que desee ejecutar: 
                    
                    """))
                    while option_adm != 1 and option_adm != 2 and option_adm != 3 and option_adm != 4:
                        option_adm = int(input("Introduzca al opcion que desee ejecutar: "))        
                    if option_adm == 1: 
                        admin.erase_op()
                    elif option_adm == 2:
                        admin.erase_oc
                    elif option_adm == 3:
                        self.erase_bu
                    elif option_adm == 0:
                        break

                else:
                    print("No esta permitido el acceso, hasta luego")
                    self.menu()

            elif option_1 == 5:
                option_esta= int(input("""
                             Menu de Estadisticas

                        1. Generar informes de publicaciones con la siguiente informacion:
                            a.Usuario con mayor cantidad de publicaciones:
                            b. Carreras con mayor cantidad de publicaciones:
                        2. Generar informes de interaccion con la siguiente informacion:
                            a. Post con la mayor cantidad de interacciones:
                            b. Usuarios con mayor comentarios inadecuados:
                        3. Eliminar un usuario que infringido multiples veces las reglas:
                            a.Uusuarios con mayor cantidad de post tumbados:
                            b.Carreras con mayor comentarios inadecuados.
                            c.Usuarios iliminados por infraccion.
                        0. Salida.
        
                    
                    """))
                while not int(option_esta) in range(0,3):
                    option_esta= int(input("Error, seleccione de nuevo"))
                if option_esta == 1:
                    self.update_post_counts()
                elif option_esta == 2:
                    pass


           
            elif option_1 == 0:
                break
                    
    def g_perfil(self):
        print("""
            GESTION DEL USUARIO
        ------------
        1. Buscador.
        5. Acceder al Usuario buscando
        2. Cambiar Informacion Personal.
        3. Borrar Datos.
        4. Cambio de sesion.
    
        0. Vuelta al Menu.
        """)
        option_2 = int(input("Ingrese una opcion: "))
        while option_2 != 1 and option_2 != 2 and option_2 != 3 and option_2 != 4 and option_2 != 5 and option_2 != 0:
            option_2 = int(input("Error, ingrese una opcion:"))

        if option_2 == 1:
            self.search_username()

        elif option_2 == 2: 
            
            print(f"""
                Nombre: {Username.get_name()}
                Apellido: {Username.get_last_name()}
                Usuario: {Username.get_username()}
                Email: {Username.get_email()}
                Major/Department: {Username.get.name()}

            """)
            op_set = input("""Seleccione los datos que desea cambiar:
                1.Nombre.
                2.Apellido.
                3.Usuario.
                4.email.
                5.Carrera.
                0.Vuelta al menu.
            """)
            while op_set != "1" and op_set != "2" and op_set != "3" and op_set != "4" and op_set != "5" and op_set != 6:
            
                if op_set == 1:
                    print("Escriba el nuevo nombre: ")
                    Username.set_name()
                elif op_set == 2:
                    print("Escriba el nuevo apellido: ")
                    Username.set_last_name(self)
                elif op_set == 3:
                    print("Escriba el nuevo usuario: ")
                    Username.set_username(self)
                elif op_set == 4:
                    print("Escriba el nuevo email: ")
                    Username.set_mail(self)
                elif op_set == 5:
                    print("Escriba la nueva carrera que esta: ")
                    Username.set_departament(self)
  
        elif option_2 == 3:
            pass
        elif option_2 == 4:
            pass
        
        elif option_2 == 0:
            pass


            erase_user = input("Sequro que desea eliminar los datos de la cuenta? S/N ")
            while erase_user != "S" and erase_user != "N":
                erase_user = input("ERROR!!,Sequro que desea eliminar los datos de la cuenta? S/N ") 
            if erase_user == "S":
                usernames.remove(user_active)

    
            welcome()

    def search_username(self, Username):
    
        d_users = []
        search_u = input("""
                    ------------BUSQUEDA-----------------

            Bienvenido a su buscador, donde podra ver a sus amigos y profesores
            
            1. Busqueda por Usuario
            2. En caso de no conocerlo, seleccione el departamento del que desea buscar.
            3. Revisar el perfil de Usuario que busco.
            0. Vuelta al menu.
        """)
        while not int(search_u) in range(0,4):
            search_u = int(input("error, seleccione de nuevo: "))
        if search_u == 1:
            s_u = input("Ingrese al usuario que desea buscar: ")
            s_users = []
            for user in self.usernames:
                if  user.username.lower() == username.lover():
                    s_users.append(user)
                

            if s_users:
                print("usuario encontrado")
                for user in s_users:
                    print(user.username)


            else:
                print("no usuario encontrado.")

        elif search_u == 2:
            department_s = input("Ponga el dpartamento o carrera que desea buscar: ")

            
            users_w = []
            for user in self.usernames:
                if user.department_s.lower() == department.lower():
                    users_w.append(user)
                
                if users_w:
                    print("encontrados en los departamentos: ")
                    for user in users_w:
                        print(user.username)
                else: 
                    print("No se encuentra en el departamento")
        
        elif search_u == 0:
            self.menu()

#Con esta funcion vemos los posts de otro usuario
    def view_posts(self, username):
        if username in user_active:
            for post in posts:
                if post.publisher == username:
                    print("Post Details:")
                    print(f"Publisher: {post.publisher}")
                    print(f"Multimedia: {post.multimedia}")
                    print(f"Caption: {post.caption}")
                    print(f"Date: {post.date}")
                    print(f"Likes: {post.likes}")
                    print(f"Comments: {post.comments}")
                    print("----------------------")
        else:
            print(f"You need to follow {username} to view their posts.")

    def search_posts(self, filter_type, search):
        if filter_type == "user":
            for post in posts:
                if post.publisher == search:
                    print("Post Details:")
                    print(f"Publisher: {post.publisher}")
                    print(f"Multimedia: {post.multimedia}")
                    print(f"Caption: {post.caption}")
                    print(f"Date: {post.date}")
                    print(f"Likes: {post.likes}")
                    print(f"Comments: {post.comments}")
                    print("----------------------")
        elif filter_type == "hashtags":
            for post in posts:
                if search in post.tags:
                    print("Post Details:")
                    print(f"Publisher: {post.publisher}")
                    print(f"Multimedia: {post.multimedia}")
                    print(f"Caption: {post.caption}")
                    print(f"Date: {post.date}")
                    print(f"Likes: {post.likes}")
                    print(f"Comments: {post.comments}")
                    print("----------------------")

    def update_post_counts(self, user_post_c, department_post_c):
        for post in posts:
            user_active.username = post.publisher
            department = user.major if user.tipo == "student" else user.department

            # Actualizar el conteo de posts del usuario
            if user in user_post_counts:
                user_post_counts[user] += 1
            else:
                user_post_counts[user] = 1

            # Actualizar el conteo de posts del dep
            if department in department_post_counts:
                department_post_counts[department] += 1
            else:
                department_post_counts[department] = 1
