from datetime import datetime

class DocumentRepository:

    def __init__(self):
        # Simulación temporal (hasta conectar SQL Server)
        self.documents = []

    # Método para crear un documento
    def create(self, titulo, codigo_documento, id_area, id_tipo):

        new_document = {
            "id_documento": len(self.documents) + 1,
            "titulo": titulo,
            "codigo_documento": codigo_documento,
            "id_area": id_area,
            "id_tipo": id_tipo,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.documents.append(new_document)

        return new_document
    
    # Método para obtener todos los documentos
    def get_all(self):
        return self.documents
    
    # Método para obtener un documento por ID
    def get_by_id(self, id_documento):
        for doc in self.documents:
            if doc["id_documento"] == id_documento:
                return doc
        return None