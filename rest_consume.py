import requests
card_number='BT1-010'

url=f'https://digimoncard.io/api-public/search.php?card={card_number}'


response=requests.request(
    method="GET",
    url=url,
    headers={"Content-Type": "application/json"},
    data={}
)
print(response.text)

#diferencias de REST y SOAP metodos , forma de acceso al servicio o endpoint SOAP es un protocolo y REST arquitectura

