from flask import Flask
from flask import request
from decouple import config
import db

app = Flask(__name__)


@app.route('/', methods=["POST"])
def enviar():
    tabela = request.args.get('tabela') or None
    dados = request.get_json()
    token = request.headers.get('Token')

    if token != config('POSTAPI_TKN'):
        return 'Token não especificado ou incorreto!'

    if tabela and dados:  # upsert
        db.enviar_dados(tabela, dados)
    else:
        return 'Método de envio desconhecido! Consulte a documentação.', 400

    return f'{len(dados)} dados enviados com sucesso!'


if __name__ == '__main__':
    app.run()
