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

@app.route('/cadastro_emoji', methods=['GET', 'POST'])
@jwt_required()
def incluir_emoji():
    try:
        print("quem está acessando: ")
        current_user = get_jwt_identity()
        print(current_user)
        
        dados = None
        if request.method == 'GET':
            return render_template("....html")
        else:
            resposta = jsonify({"resultado": "ok", "detalhes": "oi"})     
            dados = request.get_json(force = True)
            try:  
                novo = Emoji(**dados) 
                db.session.add(novo) 
                db.session.commit()  
            except Exception as e:
                resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    except Exception as e:
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        print("ERRO: "+str(e))
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        print("comecando")
        file_val = request.files['foto']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(caminho, 'imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"erro", "detalhes": str(e)})

    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

@app.route('/get_image/<int:emoji_id>')
def get_image(emoji_id):
    book = db.session.query(Emoji).get(emoji_id)
    arquivoimg = os.path.join(caminho, 'imagens/'+ book.fotoemoji)
    return send_file(arquivoimg, mimetype='image/gif')

@app.route('/fazer_login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        dados = request.get_json(force=True)
        email = str(dados['email'])
        senha = str(dados['senha'])
        print(dados)

        encontrado = Pessoa.query.filter_by(email=login, senha=senha).first()
        if encontrado is None: 
            resposta = jsonify({"resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"})
        else:
            access_token = create_access_token(identity=login)
            resposta =  jsonify({"resultado":"ok", "detalhes":access_token}) 

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

@app.route("/excluir_emoji/<int:emoji_id>", methods=['DELETE'])
def excluir_emoji(emoji_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Emoji.query.filter(Emoji.id == emoji_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/logout", methods=['POST'])
def login():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()  
    session.pop(dados['fazer_login'], default=None)
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    return resposta

app.run(debug=True, host='0.0.0.0', port=5000)