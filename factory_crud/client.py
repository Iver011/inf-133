import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate = {
    "chocolate_type":"Tableta",
    "sabor":"vainilla",
    "peso":"1gr",
}
response = requests.post(url=url, json=new_chocolate, headers=headers)
print(response.json())

new_chocolate = {
    "chocolate_type":"Bombon",
    "sabor":"vainilla",
    "peso":"5gr",
    "relleno":"crema",
}
response = requests.post(url=url, json=new_chocolate, headers=headers)
print(response.json())

response = requests.get(url=url)
print(response.json())

chocolate_id = 2
updated_vehicle_data = {
    "relleno":"menta",
}
response = requests.put(f"{url}/{chocolate_id}", json=updated_vehicle_data)
print("cambio en el chocolate realizado:", response.json())

chocolate_delete=1
response = requests.delete(f"{url}/{chocolate_delete}")
print("Chocolate eliminado:", response.json())

response = requests.get(url=url)
print(response.json())
