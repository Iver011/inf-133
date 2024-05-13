from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from databases import db
# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username= db.Column(db.String(100), unique=True, nullable=False)
    password_hash= db.Column(db.String(100), nullable=False)
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username= username
        self.set_password(password)

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
            return User.query.all()
    
    @staticmethod
    def get_user_by_username(username):
         return User.query.filter_by(username=username).first()