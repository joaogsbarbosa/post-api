from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def enviar():
    json = request.get_json()
    return request.data


if __name__ == '__main__':
    app.run()
