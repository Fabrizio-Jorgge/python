# main.py
from flask import Flask
from clientes import cliente  # Importa el blueprint correctamente

app = Flask(__name__)
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def inicio():
    return "Servidor Flask funcionando"

if __name__ == '__main__':
    # Solo accesible desde la propia máquina
    app.run(debug=True, port=5003, host='localhost')

