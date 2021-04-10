from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_login import LoginManager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ycwligxokmisto:9b5b26ef1aedede3f331103a568f4279b65aaf3a2fdc397d212cda0e29511f58@ec2-18-233-83-165.compute-1.amazonaws.com:5432/dfuvdrdjn3r8oj'
app.config['SECRET_KEY']= 'qwgy14'
login_manager=LoginManager(app)
db = SQLAlchemy(app)