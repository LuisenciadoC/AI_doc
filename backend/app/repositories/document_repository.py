from datetime import datetime
from app.config.db import get_connection

class DocumentRepository:

    def __init__(self):
        # Simulación temporal (hasta conectar SQL Server)
        self.documents = []
        self.versions = []

    # Método para crear un documento
    from app.config.db import get_connection

    def create(self, titulo, descripcion, codigo_documento, id_area, id_tipo):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO documento (titulo, descripcion, codigo_documento, id_area, id_tipo)
        VALUES (?, ?, ?, ?, ?)
        """

        cursor.execute(query, (titulo, descripcion, codigo_documento, id_area, id_tipo))
        conn.commit()

        return {
            "titulo": titulo,
            "descripcion": descripcion,
            "codigo_documento": codigo_documento,
            "id_area": id_area,
            "id_tipo": id_tipo
        }
    
    # Método para obtener todos los documentos
    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM documento")
        rows = cursor.fetchall()

        return [
            {
                "id_documento": r[0],
                "titulo": r[1],
                "descripcion": r[2],
                "codigo_documento": r[3],
                "fecha_creacion": r[4],
                "id_area": r[5],
                "id_tipo": r[6]
            }
            for r in rows
        ]
    
    # Método para obtener un documento por ID
    def get_by_id(self, id_documento):

        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM documento WHERE id_documento = ?"
        cursor.execute(query, (id_documento,))

        row = cursor.fetchone()

        if row:
            return {
                "id_documento": row[0],
                "titulo": row[1],
                "descripcion": row[2],
                "codigo_documento": row[3],
                "fecha_creacion": row[4],
                "id_area": row[5],
                "id_tipo": row[6]
            }

        return None
    
    # Método para actualizar un documento
    def update(self, id_documento, data):
        for doc in self.documents:
            if doc["id_documento"] == id_documento:
                doc["titulo"] = data.get("titulo", doc["titulo"])
                doc["codigo_documento"] = data.get("codigo_documento", doc["codigo_documento"])
                doc["id_area"] = data.get("id_area", doc["id_area"])
                doc["id_tipo"] = data.get("id_tipo", doc["id_tipo"])

                return doc
            
        return None
    
    # Método para guardar versiones (provisional)
    def save_version_history(self, document):
        self.versions.append(document)