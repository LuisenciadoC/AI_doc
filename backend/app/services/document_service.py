class DocumentService:

    def __init__(self, repository):
        self.repository = repository

    # Método para crear un documento
    def create_document(self, data):

        titulo = data.get("titulo")
        descripcion = data.get("descripcion")
        codigo_documento = data.get("codigo_documento")
        id_area = data.get("id_area")
        id_tipo = data.get("id_tipo")

        if not titulo or not codigo_documento:
            return {
                "success": False,
                "message": "Título y código son obligatorios"
            }

        return self.repository.create(
            titulo,
            descripcion,
            codigo_documento,
            id_area,
            id_tipo
        )
        
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
        
    # Método para actualizar documento
    def update_document(self, id_documento, data):

        # Buscar si existe documento
        existing = self.repository.get_by_id(id_documento)
        if not existing:
            return {
                "success": False,
                "message": "Documento no encontrado"
            }
            
        # Guardar version anterior (provisional)
        version_history = {
            "id_documento": existing["id_documento"],
            "titulo": existing["titulo"],
            "codigo_documento": existing["codigo_documento"],
            "id_area": existing["id_area"],
            "id_tipo": existing["id_tipo"] 
        }
        
        self.repository.save_version_history(version_history)
        
        #Actualizar documento
        updated = self.repository.update(id_documento, data)
        
        return {
            "success": True,
            "message": "Documento actualizado correctamente",
            "data": updated
        }
        
        