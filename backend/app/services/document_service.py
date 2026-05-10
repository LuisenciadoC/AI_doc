class DocumentService:

    def __init__(self, repository):
        self.repository = repository

    # Método para crear un documento
    def create_document(self, titulo, codigo_documento, id_area, id_tipo):

        # Validaciones básicas
        if not titulo:
            return {
                "success": False,
                "message": "El título es obligatorio"
            }

        if not codigo_documento:
            return {
                "success": False,
                "message": "El código es obligatorio"
            }

        if not id_area or not id_tipo:
            return {
                "success": False,
                "message": "Área y tipo son obligatorios"
            }

        # Enviar a repository
        document = self.repository.create(
            titulo,
            codigo_documento,
            id_area,
            id_tipo
        )

        return {
            "success": True,
            "message": "Documento creado correctamente",
            "data": document
        }
        
    # Método para visualizar documentos
    def view_documents(self):
        documents = self.repository.get_all()
        return {
            "success": True,
            "message": "Lista de documentos",
            "data": documents
        }
        
    # Método para visualizar documentos por ID
    def view_documents_id(self, id_documento):
        document = self.repository.get_by_id(id_documento)
        
        if not document:
            return {
                "success": False,
                "message": "Documento no encontrado"
            }
        
        return {
            "success": True,
            "data": document
        }