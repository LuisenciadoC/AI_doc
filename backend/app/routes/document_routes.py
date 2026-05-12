from flask import Blueprint, request, jsonify
from app.controllers.document_controller import DocumentController

#---------------document_routes.py---------------#
#En este archivo se crean las rutas donde se almacenara, consultara, creara y modificaran
#las funciones de los metodos y reciben peticiones HTTP del usuario.

document = Blueprint('document', __name__)

#Crear documento
@document.route('/create_document', methods=['POST'])
def create_document():
    # Recibir datos del frontend
    data = request.json

    # Enviar al controller
    result = DocumentController.create_document(data)
    return jsonify(result)

#---------------Ver documentos---------------#
#Ruta: /doc/view
@document.route('/view', methods=['GET'])
#Funcion para ver documentos, esta funcion obtiene los resultados del archivo document_controller.py
#El resultado se convierte en una respuesta tipo Json.
def view_documents():
    result = DocumentController.view_documents()
    return jsonify(result)


#Ruta: /doc/view/id_documento
@document.route('/view/<int:id_documento>', methods=['GET'])
#Funcion para ver documentos por medio del id, esta funcion obtiene los resultados del archivo 
#document_controller.py el resultado se convierte en una respuesta tipo Json.
def view_document_id(id_documento):
    result = DocumentController.view_document_id(id_documento)
    return jsonify(result)

#Actualizar documento
@document.route('/view_documents/<int:id_documento>/update', methods=['PUT'])
def update_document(id_documento):
    data = request.json
    result = DocumentController.update_document(id_documento, data)
    return jsonify(result)

#Eliminar documento
@document.route('/view_documents/<int:id_documento>', methods=['DELETE'])
def delete_document(id_documento):
    result = DocumentController.delete_document(
        id_documento
    )

    return jsonify(result)

@document.route('/view_documents/<int:id_documento>/restore', methods=['PUT'])
def restore_document(id_documento):
    result = DocumentController.restore_document(
        id_documento
    )

    return jsonify(result)