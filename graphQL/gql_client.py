import requests

# Definir la consulta GraphQL
query = """
    {
        estudiantes{
        id
        nombre
        apellido
        carrera
        }
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'
response = requests.post(url, json={'query': query})
print(response.text)

query = """
    {
        estudiantes{
        nombre
        }
    }
"""
response = requests.post(url, json={'query': query})
print(response.text)


query = """
    {
        estudiantes{
        nombre
        apellido
        }
    }
"""
response = requests.post(url, json={'query': query})
print(response.text)