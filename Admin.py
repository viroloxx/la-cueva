from Comment import Comment
from User import User
from Post import Post
from Api import *




class Admin:
    def __init__(self):
        self.usernames = []

    def erase_op(self, user, post):
        user = post.publisher
        user.posts.remove(post)
        return f"La publicación {post.url} ha sido eliminada."

    def erase_oc(self, user, comment):
        user = comment.user
        user.comments.remove(comment)
        #elimima el comentario ofensivo

    
    def erase_bu(self,user):
        self.usernames.remove(user)
        # Eliminar al usuario


    def report_count(self,user):

        user.infracciones += 1
        if user.infracciones >= 3:
            # Eliminar al usuario si ha infringido múltiples veces las reglas
            self.erase_bu(user, user)
            return f"El usuario {user.username} ha sido eliminado debido a múltiples infracciones."
        else:
            return f"Se ha reportado una infracción al usuario {user.username}. Infracciones actuales: {user.infracciones}"



