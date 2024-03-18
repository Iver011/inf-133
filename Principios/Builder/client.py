import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

pizza = {
    "tamaño": "Mediana",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso","Piña"]
}
response = requests.post(url, json=pizza, headers=headers)
print(response.json())