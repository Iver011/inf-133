import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}


response = requests.get(url)
print(response.json())

print("TACOS_NUEVOS \n")
mi_taco = {
    "base": "Grande",
    "guiso": "Carne",
    "salsa": "salsa golf",
    "toppings": ["Palta", "Queso"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

print("MOSTRAR_TACOS \n")
response = requests.get(url)
print(response.json())

print("EDITAR TACOS \n")
edit_taco = {
    "base":"Grande",
    "guiso": "Carne",
    "salsa": "salsa golf",
    "toppings": ["Palta", "Chile"]
}
response = requests.put(url+"/1", json=edit_taco, headers=headers)
print(response.json())

print("MOSTRAR TACOS \n")
response = requests.get(url)
print(response.json())


print("ELIMINAR TACOS \n")
response = requests.delete(url + "/1")
print(response.json())
print("MOSTRAR TACOS \n")
response = requests.get(url)
print(response.json())