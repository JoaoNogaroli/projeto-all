from inicializacao import app, db
from flask import request, render_template,redirect, url_for
import os
from classe_modelo import User, Mensagens
from flask_login import login_user, logout_user
import pusher

pusher_client = pusher.Pusher(
  app_id='1184922',
  key='172519f8f1cb46b08df5',
  secret='2097baf12c51e484c5a3',
  cluster='us2',
  ssl=True
)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def index():
    return render_template('logar.html')

@app.route("/cadastro", methods=['POST'])
def cadastro():

    nome_user = request.form['nome']
    email_user = request.form['email']
    senha_user = request.form['senha']
    if nome_user and email_user and senha_user:
        try:
            user = User(nome_user, email_user, senha_user)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('pag_logar'))
        except Exception as e:
            error = "Email já cadastrado, por favor tente outro."
            return error
    else:
        print("Error")
        return 'Error ao cadastrar'

@app.route("/logar")
def pag_logar():

    return render_template('logar.html')

@app.route("/logado")
def logado():
    #(START)---- carrega os dados da pagina
    teste = db.Table('teste',db.metadata)
    todos = db.session.query(teste).all()
    listanome=[]
    #print(todos)
    for i in todos:
        #print(i.nome_user)
        listanome.append(i.nome_user)
    pegarid = []    
    for i in todos:
        #print(i.id)
        pegarid.append(i.id)
    #(END)---- carrega os dados da pagina

    #(START) ----- Carrregar mensagens enviadas 
    mensagens = Mensagens.query.all()

    #(END) ------ Carrregar mensagens enviadas 
    return render_template('logado.html', todos=todos, mensagens = mensagens)  

@app.route("/message", methods=['POST'])
def message():
  try:
    username = request.form.get('username')
    email = request.form.get('email')
    message = request.form.get('message')
    momento =  request.form.get('momento')
    #print(username)
    #print(message)
    pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message': message})

    #(START) --- guardar dados da mensagem no banco
    
    salvar_mensagem_no_banco = Mensagens(username,email, message, momento)
    #user = User(nome_user, email_user, senha_user)
    db.session.add(salvar_mensagem_no_banco)
    db.session.commit()
    #(END) --- guardar dados da mensagem no banco
  except Exception as e:
    print(e)
  return 'ok'

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