from flask import Flask, jsonify, request

app= Flask(__name__)
#todo este codigo es una prueba de flask

@app.route("/")
def root():
    return "Hola"

"""
GET -> obtener informacion
POST -> Crear informacion
Put -> Actualizar informacion
DELETE -> Borrar informacion
"""


if __name__ == "__main__":
    app.run(debug=True)