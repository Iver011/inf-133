from flask import Blueprint,request,jsonify
from app.models.biblioteca_model import Libro
from app.views.biblioteca_view import render_libro_detail,render_libro_list
from app.utils.decorators import jwt_required,roles_required

libro_bp=Blueprint("libro",__name__)

@libro_bp.route("/libros", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_libros():
    libros=Libro.get_all()
    return jsonify(render_libro_list(libros))

@libro_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_libro(id):
    libro=Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error":"Libro no encontrado"}),404

@libro_bp.route("/libros", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_libro():
    data=request.json
    titulo=data.get("titulo")
    autor=data.get("autor")
    edicion=data.get("edicion")
    disponibilidad=data.get("disponibilidad")

    if not titulo or not autor or not edicion or not disponibilidad:
        return jsonify({"error":"Faltan datos requeridos"}),400
    
    libro=Libro(titulo=titulo,autor=autor, edicion=edicion,disponibilidad=disponibilidad)
    libro.save()


    return jsonify(render_libro_detail(libro)),201

@libro_bp.route("/libros/<int:id>", methods=["PUT"])
@roles_required(roles=["admin"])
@jwt_required
def update_libro(id):
    libro=Libro.get_by_id(id)

    if not libro:
        return jsonify({"error":"Libro no encontrado"}),404
    
    data=request.json
    titulo=data.get("titulo")
    autor=data.get("autor")
    edicion=data.get("edicion")
    disponiblidad=data.get("disponiblidad")

    libro.update(titulo=titulo,autor=autor,edicion=edicion,disponibilidad=disponiblidad)

    return jsonify(render_libro_detail(libro))


@libro_bp.route("libros/<int:id>", methods=["DELETE"])
@roles_required(roles=["admin"])
@jwt_required
def delete_libro(id):
    libro=Libro.get_by_id(id)
    if not libro:
        return jsonify({"error":"Libro no encontrado"}),404
    
    libro.delete()

    return "",204

    




