from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
        return "¡Hola, {}!".format(nombre)


def SumaDosNumeros(n1,n2):
        return n1+n2

def CadenaPalindromo(cadena):
        cadena2=cadena[::-1]
        if cadena2==cadena: return True
        else: return False

dispatcher=SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)


dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo":str},
    args={"nombre":str}
)

dispatcher.register_function(
        "SumaDosNumeros",
        SumaDosNumeros,
        returns={"suma": int},
        args={"n1":int , "n2": int}
)

dispatcher.register_function(
        "Palindromo",
        CadenaPalindromo,
        returns={"es": bool},
        args={"cadena":str}
)
server = HTTPServer(('0.0.0.0',8000),SOAPHandler)
server.dispatcher=dispatcher
print("Servidor SOAP iniciado en localhost:8000")
server.serve_forever()