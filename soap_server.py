from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHanler

def saludar(nombre):
    return "Hola!"

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

server = HTTPServer(('0.0.0.0',8000),SOAPHanler)
server.dispatcher=dispatcher
print("Servidor SOAP iniciado en localhost:8000")
server.serve_forever()