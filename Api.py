import json
import requests

from User import *
from Post import Post
from Student import Student
from Professor import Professor

# Se usa esta variable para sacar los datos de la api de usuarios
def get_users(usernames):
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json"
    r = requests.get(url)
    if r.status_code == 200:
        user_data = r.json()
#Se usa esto para extraer los datos de la api a una lista
    for user in user_data:
        dni = user["id"]
        firstName = user["firstName"]
        lastName = user["lastName"]
        email = user["email"]
        username = user["username"]
        tipo = user["type"]
        following = user["following"]
        admin = False
        if tipo == "professor":
            department = user["department"]
            user = Professor(dni, firstName, lastName, email, username, tipo, following, admin, department)
            usernames.append(user)
        else:
            major = user["major"]
            user = Student(dni, firstName, lastName, email, username, tipo, following, admin, major)
            usernames.append(user)

    #Sacar los datos de los departamentos/majors para usarlo en el buscador por filtros:



    for user in user_data:
        for k,v in user.items():
            if k=="department" and k=="jaor":
                department=v.get("department")("major")
                departments.append(department,major)

#Filas y columnas de cada estadio
    
# Se usa esta variable para sacar los datos de la api de los posts
def get_posts(posts):
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json"
    r = requests.get(url)
    if r.status_code == 200:
        post_data = r.json()
    
#Se usa esto para extraer los datos de la api a una lista
    for i in post_data:

        publisher = i["publisher"]
        tipo = i["type"]
        caption = i["caption"]
        date = i["date"]
        tags = i["tags"],
        url = i["multimedia"]["url"]
        comments = []
        likes = []

        post = Post(publisher, url, tipo, caption, date, tags, comments, likes)      
        posts.append(post)

def save_data_user(user_data, user_text):
    try: 
        with open(user_data, "w") as file:
            file.write(user_text)
        print(f"Data guardada excitosamente a {user_data}")
    except exception as e:
        print(f"An error occurred: {e}")

def save_data_post(post_data, post_text):
    try:
        with open(post_data, "w") as file:
            file.write(post_data)
        print(f"Data guardada excitosamente a {post_data}")
    except exception as e:
        print(f"An error occurred: {e}")
    
