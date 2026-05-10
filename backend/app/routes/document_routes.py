from flask import Blueprint, request, jsonify
from app.controllers.document_controller import DocumentController

document = Blueprint('document', __name__)

@document.route('/documents', methods=['POST'])

def create_document():
    # Recibir datos del frontend
    data = request.json

    # Enviar al controller
    result = DocumentController.create_document(data)

    return jsonify(result)