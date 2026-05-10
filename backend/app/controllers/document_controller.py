from app.services.document_service import DocumentService
from app.repositories.document_repository import DocumentRepository

# Instancias (inyección simple)
repo = DocumentRepository()
service = DocumentService(repo)

class DocumentController:

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