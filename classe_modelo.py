from werkzeug.security import generate_password_hash, check_password_hash
from inicializacao import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(id_user):
    return User.query.filter_by(id=id_user).first()
     

class User(db.Model, UserMixin):

    __tablename__ = 'teste'
    id = db.Column(db.Integer, primary_key=True)
    nome_user = db.Column(db.String(25), nullable=False)
    email_user = db.Column(db.String(25),nullable=False, )
    senha_user = db.Column(db.String(),nullable=False)

    def __init__(self, nome_user,email_user,senha_user):  
        self.nome_user = nome_user
        self.email_user = email_user
        self.senha_user = generate_password_hash(senha_user)

    def verify_password(self, pwd):
        return check_password_hash(self.senha_user, pwd)

class Mensagens(db.Model):
    __tablename__ = 'mensagens'
    id = db.Column(db.Integer, primary_key=True)
    nome_user = db.Column(db.String(25), nullable=False)
    email_user = db.Column(db.String(25), nullable=False)
    mensagem = db.Column(db.String(),nullable=False)    
    momento = db.Column(db.String(),nullable=False)    
    
    def __init__(self,nome_user,email_user,mensagem, momento):  
        self.nome_user = nome_user
        self.email_user = email_user
        self.mensagem = mensagem
        self.momento = momento

class Privado(db.Model):
    __tablename__ = 'privado'
    id = db.Column(db.Integer, primary_key=True)
    email_envia = db.Column(db.String(25), nullable=False)
    email_recebe = db.Column(db.String(25), nullable=False)
    mensagem = db.Column(db.String(),nullable=False)    
    momento = db.Column(db.String(),nullable=False)    
    
    def __init__(self,email_envia,email_recebe,mensagem, momento):  
        self.email_envia = email_envia
        self.email_recebe = email_recebe
        self.mensagem = mensagem
        self.momento = momento