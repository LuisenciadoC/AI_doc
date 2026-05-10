from datetime import datetime

class DocumentRepository:

    def __init__(self):
        # Simulación temporal (hasta conectar SQL Server)
        self.documents = []

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