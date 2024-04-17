import requests

url = "http://localhost:5000/"

ruta_get = url + "saludar?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)