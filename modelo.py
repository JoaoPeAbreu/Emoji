from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "pessoas.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{arquivobd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
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
    datacriacao = db.Column(db.Date)
    nomeemoji = db.Column(db.String(254))
    representacao = db.Column(db.String(254))
    fotoemoji = db.Column(db.Text)
    classificacao = db.Column(db.String(254))

    def __str__(self):
        return self.pessoa + "[id="+str(self.id)+ "], " +\
            self.datacriacao + ", " + self.nomeemoji + ", " + self.representacao +\
                self.fotoemoji + ", " + self.classificacao
    
    def json(self):
        return {
            "id": self.id,
            "pessoa": self.pessoa,
            "datacriacao": self.datacriacao,
            "nomeemoji": self.nomeemoji,
            "representacao": self.representacao,
            "fotoemoji": self.fotoemoji,
            "classificacao": self.classificacao
        }

class Gradico(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    legenda = db.Column(db.String(254))
    x = db.Column(db.Date)
    y = db.Column(db.String(254))

    def __str__(self):
        return self.legenda + "[id="+str(self.id)+ "], " +\
            self.x + ", " + self.y 
    
    def json(self):
        return {
            "id": self.id,
            "legenda": self.legenda,
            "x": self.x,
            "y": self.y
        }

class Sugestao(db.Model):
    id = id = id = db.Column(db.Integer, primary_key=True)
    id_ = db.Column(db.Integer(254))
    catalogacao = db.Column(db.String(254))
    ideia = db.Column(db.String(254))

    def __str__(self):
        return self.id + "[id="+str(self.id)+ "], " +\
            self.catalogacao + ", " + self.ideia

    def json(self):
        return {
            "id": self.id,
            "catalogacao": self.catalogacao,
            "ideia": self.ideia
        }

"""class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    nome_foto = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.nome_foto
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "nome_foto": self.nome_foto
        }"""