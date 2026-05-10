import re

from app.services.document_service import DocumentService
from app.repositories.document_repository import DocumentRepository

# Instancias (inyección simple)
repo = DocumentRepository()
service = DocumentService(repo)

class DocumentController:

    # Métodos estáticos para manejar las solicitudes de creación del frontend
    @staticmethod
    def create_document(data):

        titulo = data.get("titulo")
        codigo_documento = data.get("codigo_documento")
        id_area = data.get("id_area")
        id_tipo = data.get("id_tipo")

        return service.create_document(
            titulo,
            codigo_documento,
            id_area,
            id_tipo
        )
        
    # Métodos para manejar las solicitudes de visualización del frontend
    @staticmethod
    def view_documents():
        return service.view_documents()
    
    # Métodos para manejar las solicitudes de visualización del frontend por ID
    @staticmethod
    def view_document_id(id_documento):
        return service.view_documents_id(id_documento)