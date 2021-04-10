from inicializacao import app, db
from flask import request, render_template,redirect, url_for
import os
from classe_modelo import User
from flask_login import login_user, logout_user

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=['POST'])
def cadastro():

    nome_user = request.form['nome']
    email_user = request.form['email']
    senha_user = request.form['senha']
    if nome_user and email_user and senha_user:
        user = User(nome_user, email_user, senha_user)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('pag_logar'))
    else:
        print("Error")
        return 'Error ao cadastrar'

@app.route("/logar")
def pag_logar():

    return render_template('logar.html')

@app.route("/logado")
def logado():

    return render_template('logado.html')   

@app.route("/logar_user", methods=['POST'])
def logar_user():

    email_user = request.form['email']
    senha_user = request.form['senha']

    user =  User.query.filter_by(email_user=email_user).first()

    """try:
        login_user(user)
        return render_template('logado.html')
    except Exception as e:
        print(e)
        return render_template('logar.html')"""
    if not user or not user.verify_password(senha_user):
        print(user)
        print("SENHA: ", senha_user)
        return 'Não logado'
    
    login_user(user)
    return redirect(url_for('logado'))

 

if __name__ == "__main__":
    app.run(debug=True, port=port)