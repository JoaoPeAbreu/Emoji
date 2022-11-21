from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import *
from datetime import date
import os
from flask_session import *

app = Flask(__name__)
meuservidor = "http://localhost:8080"
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, 'tabelas.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

app.secret_key = '$#EWFGHJUI*&DEGBHYJU&Y%T#RYJHG%##RU&U'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from datetime import timedelta

app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
jwt = JWTManager(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    def __str__(self):
        return self.nome + "[id=" + str(self.id) + "], " +\
            self.email + ", " + self.senha

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }

class Emoji(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    dcria = db.Column(db.Date) #data criação
    nemo = db.Column(db.String(254)) #nome emoji
    repre = db.Column(db.String(254)) #representação
    femo = db.Column(db.Text) #foto emoji
    classi = db.Column(db.String(254)) #classificação

    def __str__(self):
        return str(self.pessoa) + "[id=" + str(self.id)+ "], " +\
            str(self.dcria) + ", " + self.nemo + ", " + self.repre +\
                self.femo + ", " + self.classi
    
    def json(self):
        return {
            "id": self.id,
            "pessoa_id": self.pessoa_id,
            "pessoa": self.pessoa.json(),
            "dcria": self.dcria,
            "nemo": self.nemo,
            "repre": self.repre,
            "femo": self.femo,
            "classi": self.classi
        }

class Sugestao(db.Model):
    id = id = id = db.Column(db.Integer, primary_key=True)
    catalogacao = db.Column(db.String(254))
    ideia = db.Column(db.String(254))

    def __str__(self):
        return "[id=" + str(self.id)+ "], " +\
            self.catalogacao + ", " + self.ideia

    def json(self):
        return {
            "catalogacao": self.catalogacao,
            "ideia": self.ideia
        }

'''if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Pessoa(nome = "Akemi", email = "akemi.shibukawa@gmail.com", senha = "antilopes1galopantes")
    p2 = Pessoa(nome = "João", email = "joao.abreu@gmail.com", senha = "luzes1para2o3mundo")

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    print(".....................................")
    print(p1)
    print(p2)
    print(".....................................")

    e1 = Emoji(pessoa = p1, dcria = date(2022, 10, 3), nemo = "coelho", repre = "O emoji representa um coelho femea", classi = "Animais", femo= 'sla')
    e2 = Emoji(pessoa = p2, dcria = date(2022, 10, 2), nemo = "pinheiro", repre = "O emoji representa o pinheiro que fica na minha casa", classi = "Planta", femo= 'sla2')

    db.session.add(e1)
    db.session.add(e2)
    db.session.commit()

    print(".....................................")
    print(e1)
    print(e2)
    print(".....................................")

    s1 = Sugestao(catalogacao = "Planta", ideia = "Samambaia")
    s2 = Sugestao(catalogacao = "Expressões", ideia = "Sorridente")

    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

    print(".....................................")
    print(s1)
    print(s2)
    print(".....................................")'''