from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(id_user):
    return User.query.filter_by(id=id_user).first()
     

class User(db.Model, UserMixin):

    __tablename__ = 'teste'
    id = db.Column(db.Integer, primary_key=True)
    nome_user = db.Column(db.String(25), nullable=False)
    email_user = db.Column(db.String(25),nullable=False, unique=True)
    senha_user = db.Column(db.String(),nullable=False)

    def __init__(self, nome_user,email_user,senha_user):  
        self.nome_user = nome_user
        self.email_user = email_user
        self.senha_user = generate_password_hash(senha_user)

    def verify_password(self, pwd):
        return check_password_hash(self.senha_user, pwd)

    