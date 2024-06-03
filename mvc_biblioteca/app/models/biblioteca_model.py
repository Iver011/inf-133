from app.database import db

class Libro(db.Model):
    __tablename__="libros"

    id=db.Column(db.Integer,primary_key=True)
    titulo=db.Column(db.String(100), nullable=False)
    autor=db.Column(db.String(100),nullable=False)
    edicion=db.Column(db.String(100),nullable=False)
    disponibilidad=db.Column(db.String(50),nullable=False)

#iniciamos la clase

    def __init__(self,titulo,autor,edicion,disponibilidad):
        self.titulo=titulo
        self.autor=autor
        self.edicion=edicion
        self.disponibilidad=disponibilidad

    #guardar un libro

    def save(self):
        db.session.add(self)
        db.session.commit()

    #obtener la lista de libros
    @staticmethod
    def get_all():
        return Libro.query.all()
    
    #obtener uno solo por id
    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)
    

    #actualizar datos
    def update(self, titulo=None, autor=None, edicion=None, disponibilidad=None):
        if titulo is not None:
            self.titulo=titulo
        if autor is not None:
            self.autor=autor
        if edicion is not None:
            self.edicion=edicion
        if disponibilidad is not None:
            self.disponibilidad=disponibilidad
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()
    