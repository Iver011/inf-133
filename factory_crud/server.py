from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class DeliveryChocolate:
    def __init__(self,chocolate_type, sabor, peso, relleno=""):
        self.chocolate_type=chocolate_type
        self.sabor=sabor
        self.peso=peso
        self.relleno=relleno
        


class Tabletas(DeliveryChocolate):
    def __init__(self, sabor,peso):
        super().__init__("Tableta", sabor,peso)
        

class Bombones(DeliveryChocolate):
    def __init__(self, sabor,peso,relleno):
        super().__init__("Bombon", sabor,peso)
        self.relleno=relleno

class Trufas(DeliveryChocolate):
    def __init__(self, sabor,peso,relleno):
        super().__init__("Trufa", sabor,peso)
        self.relleno=relleno


class DeliveryFactory:
    @staticmethod
    def create_chocolate(chocolate_type,sabor,peso,relleno=None):
        if chocolate_type == "Tableta":
            return Tabletas(sabor,peso)
        elif chocolate_type == "Bombon":
            return Bombones(sabor,peso,relleno)
        elif chocolate_type == "Trufa":
            return Trufas(sabor,peso,relleno)
        else:
            raise ValueError("Tipo de chocolate de entrega no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class DeliveryService:
    def __init__(self):
        self.factory = DeliveryFactory()
        
        self.chocolate_counter = 1

    def add_chocolate(self, data):
        
        chocolate_type = data.get("chocolate_type", None)
        sabor = data.get("sabor", None)
        peso= data.get("peso",None)
        relleno = data.get("relleno", None) if chocolate_type in ["Bombon", "Trufa"] else None        

        delivery_chocolate = self.factory.create_chocolate(
            chocolate_type,sabor,peso,relleno
        )
        chocolates[self.chocolate_counter] = delivery_chocolate
        self.chocolate_counter += 1
        
        return delivery_chocolate

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            sabor = data.get("sabor", None)
            peso = data.get("peso", None)
            if chocolate.chocolate_type in ["Bombon", "Trufa"]:
                relleno = data.get("relleno", None)
                if relleno is not None:
                    chocolate.relleno = relleno
            if sabor:
                chocolate.sabor = sabor
            if peso:
                chocolate.peso = peso
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "chocolate eliminado"}
        else:
            return None


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.delivery_service = DeliveryService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.delivery_service.list_chocolates()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_chocolate(chocolate_id,data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "elemento no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "elemento no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()