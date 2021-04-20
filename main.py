from flask import Flask
from flask import request
import db

app = Flask(__name__)


@app.route('/', methods=["POST"])
def enviar():
    dados = request.get_json()
    tabela = request.args.get('tabela') or None
    pk = request.args.get('pk') or None

    if tabela and pk:  # upsert
        db.conectar().upsert(tabela, dados, pk)
    else:
        return 'Método de envio desconhecido! Consulte a documentação.', 400

    return f'{len(dados)} dados enviados com sucesso!'


if __name__ == '__main__':
    app.run()
