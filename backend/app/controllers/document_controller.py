from app.services.document_service import DocumentService
from app.repositories.document_repository import DocumentRepository

# Instancias (inyección simple)
repo = DocumentRepository()
service = DocumentService(repo)

class DocumentController:

    # Métodos estáticos para manejar las solicitudes de creación del frontend
    @staticmethod
    def create_document(data):
        return service.create_document(data)
        
    # Métodos para manejar las solicitudes de visualización del frontend
    @staticmethod
    def view_documents():
        return service.view_documents()
    
    # Métodos para manejar las solicitudes de visualización del frontend por ID
    @staticmethod
    def view_document_id(id_documento):
        return service.view_documents_id(id_documento)
    
    # Métodos para actualizar documento
    @staticmethod
    def update_document(id_documento, data):
        return service.update_document(id_documento, data)
    
    # Métodos para eliminar documento
    @staticmethod
    def delete_document(id_documento):
        return service.delete_document(id_documento)