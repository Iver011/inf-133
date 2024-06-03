def test_get_libros_user(test_client,user_auth_headers):
    response=test_client.get("/api/libros", headers=user_auth_headers)
    assert response.status_code==200
    assert response.json==[]


def test_created_libro_user(test_client, user_auth_headers):
    data={"titulo":"El alquimista", "autor":"cohelo", "edicion":"2012", "disponibilidad":"si"}
    response=test_client.post("/api/libros", json=data, headers=user_auth_headers)
    assert response.status_code==403

def test_update_libro_user(test_client, user_auth_headers):
    data={"titulo":"El alquimista", "autor":"cohelo", "edicion":"2012", "disponibilidad":"si"}
    response=test_client.put("/api/libros/1", json=data, headers=user_auth_headers)
    assert response.status_code==403

def test_delete_libro_user(test_client, user_auth_headers):
    response=test_client.delete("/api/libros/1", headers=user_auth_headers)
    assert response.status_code==403