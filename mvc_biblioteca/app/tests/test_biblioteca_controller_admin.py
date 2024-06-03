def test_get_libros(test_client,admin_auth_headers):
    response= test_client.get("/api/libros", headers=admin_auth_headers)
    assert response.status_code==200
    assert response.json==[]

def test_create_libro(test_client,admin_auth_headers):
    data={"titulo":"La migala", "autor":"Arreola", "edicion":"1980", "disponibilidad":"si"}
    response=test_client.post("/api/libros" ,json=data, headers=admin_auth_headers)
    assert response.status_code==201
    assert response.json["titulo"]=="La migala"
    assert response.json["autor"]=="Arreola"
    assert response.json["edicion"]=="1980"
    assert response.json["disponibilidad"]=="si"

def test_get_libro(test_client,admin_auth_headers):
    data={"titulo":"las olas", "autor":"wolf", "edicion":"2000", "disponibilidad":"si"}
    response=test_client.post("/api/libros" , json=data, headers=admin_auth_headers)
    assert response.status_code==201
    libro_id=response.json["id"]

    response=test_client.get(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code==200
    assert response.json["titulo"]=="las olas"
    assert response.json["autor"]=="wolf"
    assert response.json["edicion"]=="2000"
    assert response.json["disponibilidad"]=="si"

def test_nonexistent_libro(test_client,admin_auth_headers):
    response=test_client.get("/api/libros/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code==404
    assert response.json["error"]=="Libro no encontrado"

def test_created_libro_invalid_data(test_client,admin_auth_headers):
    data={"titulo":"el extranjero"}
    response=test_client.post("/api/libros", json=data , headers=admin_auth_headers)
    assert response.status_code==400
    assert response.json["error"]=="Faltan datos requeridos"


def test_update_libro(test_client,admin_auth_headers):
    data={"titulo":"1984", "autor":"camus", "edicion":"2000", "disponibilidad":"si"}
    response=test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code==201
    libro_id=response.json["id"]

    update_data={"titulo":"1984", "autor":"orwell", "edicion": "1965", "disponibilidad":"si"}
    response=test_client.put(f"/api/libros/{libro_id}",json=update_data, headers=admin_auth_headers)
    assert response.status_code==200
    assert response.json["titulo"]=="1984"
    assert response.json["autor"]=="orwell"
    assert response.json["edicion"]=="1965"
    assert response.json["disponibilidad"]=="si"


def test_update_nonexistent_libro(test_client,admin_auth_headers):
    update_data={"titulo":"metamorfosis", "autor":"kafka","edicion":"2001", "disponibilidad":"no"}
    response=test_client.put("/api/libros/999", json=update_data, headers=admin_auth_headers)
    print(response.json)
    assert response.status_code==404
    assert response.json["error"]=="Libro no encontrado"

def test_delete_libro(test_client,admin_auth_headers):
    data={"titulo":"farenheit", "autor":"anonimo", "edicion": "1999", "disponibilidad":"no"}
    response=test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code==201
    libro_id=response.json["id"]

    response=test_client.delete(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code==204
    
    response=test_client.get(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code==404
    assert response.json["error"]=="Libro no encontrado"


def test_nonexistent_libro(test_client, admin_auth_headers):
    response=test_client.delete("/api/libros/999", headers=admin_auth_headers)
    assert response.status_code==404
    assert response.json["error"]=="Libro no encontrado"


    
