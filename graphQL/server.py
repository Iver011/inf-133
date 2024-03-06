from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int,List,Schema
#HTTPSERVER nos dice donde vive el servidor almacena la direccion del puerto
#BaseHTTP determina las solicitures, se encarga de recibir y dar la respuesta
#lee lo que llega que es texto plano a algo mas manejable
#ObjectType se puede heredar y da los tipos de datos que maneja la clase y campos es decir crea un objeto con varios campos
#y a cada campo darle un tipo de dato
#List objeto que puede almacerar multiples datos
#Schema da toda las consultas posibles, y el como se intercambia la info es a cargo del ObjectType


class Query(ObjectType):
    hello=String()
    goodbye= String()
    def resolve_hello(root,info):
        return 'Hello World!'
    
    def resolve_goodbye(root,info):
        return 'Bye,Bye'
    

schema=Schema(query=Query)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()


