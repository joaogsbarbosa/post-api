from flask import Flask
from flask import request
import db

app = Flask(__name__)


@app.route('/', methods=["POST"])
def enviar():
    tabela = request.args.get('tabela') or None
    dados = request.get_json()
    pk = request.args.get('pk') or None

    if tabela and dados and pk:  # upsert
        db.enviar_dados(tabela, dados, pk)
    else:
        return 'Método de envio desconhecido! Consulte a documentação.', 400

    return f'{len(dados)} dados enviados com sucesso!'


if __name__ == '__main__':
    app.run()
