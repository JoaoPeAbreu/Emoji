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

app.run(debug=True, host='0.0.0.0', port=5000)