from flask import Flask, jsonify, request, send_file, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
import os
app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "tabelas.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{arquivobd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)

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
    datacriacao = db.Column(db.Date)
    nomeemoji = db.Column(db.String(254))
    representacao = db.Column(db.String(254))
    fotoemoji = db.Column(db.Text)
    classificacao = db.Column(db.String(254))

    def __str__(self):
        return str(self.pessoa) + "[id=" + str(self.id)+ "], " +\
            str(self.datacriacao) + ", " + self.nomeemoji + ", " + self.representacao +\
                self.fotoemoji + ", " + self.classificacao
    
    def json(self):
        return {
            "id": self.id,
            "pessoa_id": self.pessoa_id,
            "pessoa": self.pessoa.json(),
            "datacriacao": self.datacriacao,
            "nomeemoji": self.nomeemoji,
            "representacao": self.representacao,
            "fotoemoji": self.fotoemoji,
            "classificacao": self.classificacao
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

if __name__ == "__main__":
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

    e1 = Emoji(pessoa = p1, datacriacao = date(2022, 10, 3), nomeemoji = "coelho", representacao = "O emoji representa um coelho femea", classificacao = "Animais", fotoemoji= 'sla')
    e2 = Emoji(pessoa = p2, datacriacao = date(2022, 10, 2), nomeemoji = "pinheiro", representacao = "O emoji representa o pinheiro que fica na minha casa", classificacao = "Planta", fotoemoji= 'sla2')

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
    print(".....................................")