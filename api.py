from flask import Flask, jsonify, request
import json
app = Flask(__name__)


def ler_contatos():
            try:
                with open("dados.json",'r') as file:
                    contatos = json.load(file)
            except:
                contatos = []
            return contatos
    
contatos_atualizados = ler_contatos()
@app.route('/dados',methods=['GET'])
def obter_livros():
    return jsonify(contatos_atualizados)


@app.route('/dados/<string:nome>',methods=['GET'])
def obter_por_nome(nome):
     for dado in contatos_atualizados:
           if dado.get('nome') == nome:
                 return jsonify(dado)


if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)