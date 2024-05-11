from flask import Flask, request, jsonify
from gauss_jordan import gauss_jordanv2, obtener_col
from flask_cors import CORS
from flask_cors import cross_origin

from optimizar import optimizar_resultado


app = Flask(__name__)

CORS(app) #para que el servidor de dasarrollo de react se comumique con el servidor de desarollo de flask
@app.route("/")
def hello_world():
    return "Hola Flask"


@app.route("/gauss_jordan", methods=['POST'])
def gauss_jordan():
    matriz = request.json["matriz"]
    gauss_jordanv2(matriz)
    resultado = list(optimizar_resultado(matriz)) 

    return jsonify(
            {"respuesta": resultado}
            )



if __name__ == "__main__":
    app.run(debug=True, port=4000, host='0.0.0.0')
