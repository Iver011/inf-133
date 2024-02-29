import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)

ruta_eliminar= url +"estudiantes"
eliminar_response=requests.request(method="DELETE",
                                   url=ruta_eliminar)
print(eliminar_response.text)

ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)


ruta_put= url + "estudiantes"
estudiante_actualizado={
    "id":1,
    "nombre": "Juan",
    "apellido":"Perez",
    "carrera":"Ingeniera Ambiental"
}
put_response = requests.request(method="PUT"
                                ,url=ruta_put,
                                json=estudiante_actualizado)
print(put_response.text)

ruta_filtrar_id=url+"estudiantes/2"
filtro_response=requests.request(method="GET",
                                 url=ruta_filtrar_id)
print(filtro_response.text)

ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
ruta_carreras=url + "carreras"
carreras_response=requests.request(method="GET",
                                   url=ruta_carreras)
print(carreras_response.text)


ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Manuel",
    "apellido": "Sanchez",
    "carrera": "Economia",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Carlos",
    "apellido": "Navia",
    "carrera": "Economia",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)


get_response= requests.request(method="GET",
                               url=ruta_get)

print(get_response.text)

ruta_filtro_carrera=url + "carreras/Economia"
filtro_carrera_response=requests.request(method="GET",
                                         url=ruta_filtro_carrera)

print(filtro_carrera_response.text)
