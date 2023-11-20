class Post:
    def __init__(self, publisher:str, url: str, tipo: str, caption: str, date: int, tags: str, comments, likes):
        self.publisher = publisher
        self.url = url
        self.tipo = tipo
        self.caption = caption 
        self.date = date
        self.tags = tags
        self.comments = comments
        self.likes = likes


#------------------IMPRIMIR LOS DATOS-----------------------------------------------------
    def show_post(self):
        return f"""
   
        Nombre: {self.publisher} 
        tipo de media: {self.tipo}
        Descripcion: {self.caption} 
        Hashtag: {self.tags}
        Fechas : {self.date}
        
        
        """


    def get_publisher(self):
        return self.publisher

    def get_tipo(self):
        return self.tipo

    def get_caption(self):
        return self.caption

    def get_tags(self):
        return self.tags
        
    def get_date(self):
        return self.date

#-------------------likes---------------------------------------------
        
        
        
                