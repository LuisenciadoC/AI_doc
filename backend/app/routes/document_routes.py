from flask import Blueprint, request, jsonify
from app.controllers.document_controller import DocumentController

document = Blueprint('document', __name__)

#Crear documento
@document.route('/create_document', methods=['POST'])
def create_document():
    # Recibir datos del frontend
    data = request.json

    # Enviar al controller
    result = DocumentController.create_document(data)
    return jsonify(result)

#Ver documentos
@document.route('/view_documents', methods=['GET'])
def view_documents():
    result = DocumentController.view_documents()
    return jsonify(result)

#Ver documento por ID
@document.route('/view_documents/<int:id_documento>', methods=['GET']) #probar cambiar id por codigo
def view_document_id(id_documento):
    result = DocumentController.view_document_id(id_documento)
    return jsonify(result)

#Actualizar documento
@document.route('/view_documents/<int:id_documento>/update', methods=['PUT'])
def update_document(id_documento):
    data = request.json
    result = DocumentController.update_document(id_documento, data)
    return jsonify(result)