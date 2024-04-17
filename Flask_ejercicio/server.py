#FrameWork: Marco de Trabajo
#Flask: microframework web para python/ pip install Flask/ las clases siempre inician en Mayuscula, las librerias y otros en min
from flask import Flask, request, jsonify 
app = Flask(__name__)
@app.route('/sumar', methods=['GET']) #decorador: asocia la ruta con la funcion, por defecto es get
def sumar():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    print(num1,num2)
    if not num1 or not num2:
        return (
            jsonify({"error":"Uno de los parametros no fue encontrado"}),400,
        )
    return jsonify({"Resultado de la suma":f"{int(num1)+int(num2)}"})
@app.route('/palindromo', methods=['GET']) #decorador: asocia la ruta con la funcion, por defecto es get
def palindromo():
    cadena = request.args.get('cadena')
    
    if not cadena:
        return (
            jsonify({"error":"Uno de los parametros no fue encontrado"}),400,
        )
    cadena = cadena.lower().replace(" ", "")
    cadena_inv=cadena[::-1]

    if cadena == cadena_inv:
        return jsonify({"Message":f"la palabra {cadena} es palindromo"})
    else:
        return jsonify({"Message":f"la palabra {cadena} NO es palindromo"})
    
@app.route('/contar', methods=['GET']) #decorador: asocia la ruta con la funcion, por defecto es get
def contar():
    cadena = request.args.get('cadena')
    vocal= request.args.get('vocal')
    if not cadena or not vocal:
        return (
            jsonify({"error":"Uno de los parametros no fue encontrado"}),400,
        )
    cadena = cadena.lower()
    vocal = vocal.lower()
    
    contador = cadena.count(vocal)
    return jsonify({"Message":f"la vocal {vocal} se repite {contador} veces"})

if __name__ == '__main__':  #se aloja en el localhost:5000
    app.run() 

