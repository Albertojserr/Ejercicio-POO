class Libro():
    fecha=0
    titulo=""
    autor=""
    editorial=""
    ISBN=""
    def __init__(self,titulo,autor,fecha,editorial,ISBN):
        self.titulo=titulo
        self.autor=autor
        self.fecha=fecha
        self.editorial=editorial
        self.ISBN=ISBN


    def setTitulo(self,titulo):
        self.titulo=titulo

    def setAutor(self,autor):
        self.autor=autor

    def setFecha(self,fecha):
        self.fecha=fecha

    def setEditorial(self,editorial):
        self.editorial=editorial

    def setISBN(self,ISBN):
        self.ISBN=ISBN
