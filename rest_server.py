from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes =[
    {
        "id"=1,
        "nombre":"Pedrito",
        "apellido":"Garcia",
        "Carrera": "Administracion de Empresas",
    },
]

class RESTRH(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers(json.dumps(estudiantes).encode('utf-8'))

def run_server(port=8000):
    try:
        server_address=('',port)
        httpd=HTTPServer(server_address,RESTRH)
        print(f'Iniciando servidor web en localhost')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("apagando")
        httpd.socket.close()

        
