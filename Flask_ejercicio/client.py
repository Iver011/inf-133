import requests

url = "http://localhost:5000/"

ruta_get = url + "sumar?num1=5&num2=3"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


ruta_get = url + "palindromo?cadena=reconocer"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


ruta_get = url + "contar?cadena=exepciones&vocal=e"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
