#FrameWork: Marco de Trabajo
#Flask: microframework web para python/ pip install Flask/ las clases siempre inician en Mayuscula, las librerias y otros en min
from flask import Flask, request, jsonify 
app = Flask(__name__)
@app.route('/saludar', methods=['GET']) #decorador: asocia la ruta con la funcion, por defecto es get
def saludar():
    nombre = request.args.get('nombre')
    if not nombre:
        return (
            jsonify({"error":"Se requiere un nombre en los parametros de la URL."}),400,
        )
    return jsonify({"mensaje":f"Hola, {nombre}"})
if __name__ == '__main__':  #se aloja en el localhost:5000
    app.run() 







