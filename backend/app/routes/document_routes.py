from flask import Blueprint, request, jsonify
from app.controllers.document_controller import DocumentController

#---------------document_routes.py---------------#
#En este archivo se crean las rutas donde se almacenara, consultara, creara y modificaran
#las funciones de los metodos y reciben peticiones HTTP del usuario.

document = Blueprint('document', __name__)


#---------------Crear documentos---------------#
#Ruta: /doc/create
#Funcion para crear documentos, esta funcion obtiene los resultados del archivo document_controller.py
#El resultado se convierte en una respuesta tipo Json.
@document.route('/create', methods=['POST'])
def create_document():
    #Recibir datos del frontend.
    data = request.json

    #Enviar al controller.
    result = DocumentController.create_document(data)
    return jsonify(result)


#---------------Ver documentos---------------#
#Ruta: /doc/view
@document.route('/view', methods=['GET'])
#Funcion para ver documentos, esta funcion obtiene los resultados del archivo document_controller.py
#El resultado se convierte en una respuesta tipo Json.
def view_documents():
    #Enviar al controller.
    result = DocumentController.view_documents()
    return jsonify(result)

#Ruta: /doc/view/id_documento
@document.route('/view/<int:id_documento>', methods=['GET'])
#Funcion para ver documentos por medio del id, esta funcion obtiene los resultados del archivo 
#document_controller.py el resultado se convierte en una respuesta tipo Json.
def view_document_id(id_documento):
    #Enviar al controller.
    result = DocumentController.view_document_id(id_documento)
    return jsonify(result)

#Ruta: /doc/view/codigo_documento
@document.route('/view/<string:codigo_documento>', methods=['GET'])
#Funcion para ver documentos por medio del codigo, esta funcion obtiene los resultados del archivo 
#document_controller.py el resultado se convierte en una respuesta tipo Json.
def view_document_cod(codigo_documento):
    #Enviar al controller.
    result = DocumentController.view_document_cod(codigo_documento)
    return jsonify(result)


#---------------Actualizar documentos---------------#
#Ruta: /doc/view/id_documento/update
@document.route('/view/<int:id_documento>/update', methods=['PUT'])
#Funcion para actualizar documentos por medio del id, esta funcion obtiene los resultados del archivo 
#document_controller.py el resultado se convierte en una respuesta tipo Json.
def update_by_id(id_documento):
    data = request.json
    return jsonify(DocumentController.update_by_id(id_documento, data))

#Ruta: /doc/view/codigo_documento/update
@document.route('/view/<string:codigo_documento>/update', methods=['PUT'])
#Funcion para actualizar documentos por medio del id, esta funcion obtiene los resultados del archivo 
#document_controller.py el resultado se convierte en una respuesta tipo Json.
def update_by_cod(codigo_documento):
    data = request.json
    return jsonify(DocumentController.update_by_cod(codigo_documento, data))


#---------------Eliminar documentos---------------#
#Ruta: /doc/view/id_documento
#Funcion para eliminar documentos por medio del id, esta funcion obtiene los resultados del archivo 
#document_controller.py el resultado se convierte en una respuesta tipo Json.
@document.route('/view/<int:id_documento>', methods=['DELETE'])
def delete_by_id(id_documento):
    result = DocumentController.delete_by_id(id_documento)
    return jsonify(result)


#---------------Restaurar documentos---------------#
#Ruta: /doc/view/id_documento/restore
@document.route('/view/<int:id_documento>/restore', methods=['PUT'])
def restore_document(id_documento):
    result = DocumentController.restore_document(id_documento)
    return jsonify(result)