import requests

url='http://localhost:8000/'

ruta_post=url+'estudiantes'
nuevo_estudiante={
    'nombre':'Juan',
    'apellido':'Perez',
    'carrera':'Economia',
    
}
post_response=requests.request(method='POST',url=ruta_post,
                               json=nuevo_estudiante)

print(post_response.text)


ruta_get=url + 'estudiantes'
get_response=requests.request(method='GET', url=ruta_get)
print(get_response.text)


print("BUSQUEDA POR NOMBRE:  ")

ruta_get=url + 'estudiantes?nombre=Pedrito'
get_response=requests.request(method='GET', url= ruta_get)
print(get_response.text)

print("BUSQUEDA POR APELLIDO: ")
ruta_get=url+'estudiantes?apellido=Perez'
get_response=requests.request(method='GET', url=ruta_get)
print(get_response.text)

ruta_post=url+ 'estudiantes'
nuevo_estudiante={
    'nombre':'Elvis',
    'apellido':'Perez',
    'carrera':'Arquitectura',
}
post_response=requests.request(method='POST',
                            url=ruta_post,
                            json=nuevo_estudiante)


print("ESTUDIANTES POR NOMBRE Y APELLIDO")
ruta_get=url+ 'estudiantes?nombre=Elvis&apellido=Perez'
get_response=requests.request(method='GET',
                            url=ruta_get)
print(get_response.text)

