from modelo import *

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def incluir_pessoa():
    if request.method == 'GET':
        return render_template("cadastro.html")
    else:
        resposta = jsonify({"resultado": "ok", "detalhes": "oi"})     
        dados = request.get_json(force = True)
        try:  
            nova = Pessoa(**dados) 
            db.session.add(nova) 
            db.session.commit()  
        except Exception as e:
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta 

@app.route('/fazer_login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        dados = request.get_json(force=True)
        email = str(dados['email'])
        senha = str(dados['senha'])
        print(dados)

        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Emoji":
      dados = db.session.query(Emoji).all()
    lista_jsons = [ x.json() for x in dados ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta

@app.route("/atualizar_emoji/<string:classe>", methods=['put'])
def atualizar(classe):
    if request.method == 'GET':
        return render_template("atualizaremoji.html")
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()  
    try:  
        if classe == "Emoji":
            if 'id' not in dados:
                resposta = jsonify({"resultado": "erro", 
                            "detalhes": "Atributo id não encontrado"})
            else:
                id = dados['id']
                algo = Emoji.query.get(id)
                if algo is None:
                    resposta = jsonify({"resultado": "erro", 
                                "detalhes": f"Objeto não encontrado, id: {id}"})
                else:
                    algo.datacriacao = dados['datacriacao']
                    algo.nomeemoji = dados['nomeemoji']
                    algo.representacao = dados['representacao']
                    algo.fotoemoji = dados['fotoemoji']
                    algo.classificacao = dados['classificacao']
                    db.session.commit()
        else:
            resposta = jsonify({"resultado": "erro", "detalhes": f"Classe não encontrada: {classe}"})        
        
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True, host='0.0.0.0', port=5000)