from datetime import datetime
from app.config.db import get_connection

class DocumentRepository:

    from app.config.db import get_connection

    def __init__(self):
        # Simulación temporal (hasta conectar SQL Server)
        self.documents = []
        self.versions = []

    # Método para crear un documento
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

        query = """
        SELECT * FROM documento
        WHERE estado = 1
        """

        cursor.execute(query)
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

        query = query = """
        SELECT * 
        FROM documento 
        WHERE id_documento = ?
        AND estado = 1
        """
        
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
        
# Métodos para eliminar documentos
    # Hard delete (menor a 36 horas)
    def hard_delete(self, id_documento):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM documento WHERE id_documento = ?"
        
        cursor.execute(query, (id_documento,))
        conn.commit()
    
    # Soft delete (mayores a 36 horas)
    def soft_delete(self, id_documento):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        UPDATE documento
        SET estado = 0
        WHERE id_documento = ?
        """
        
        cursor.execute(query, (id_documento,))
        conn.commit() 
        
    # Método para buscar documentos para IA
    def search_documents(self, question):

        conn = get_connection()
        cursor = conn.cursor()

        # Separar palabras
        words = question.split()

        conditions = []
        values = []

        # Crear LIKE dinámicos
        for word in words:

            conditions.append("titulo LIKE ?")
            conditions.append("descripcion LIKE ?")

            values.append(f"%{word}%")
            values.append(f"%{word}%")

        query = f"""
        SELECT *
        FROM documento
        WHERE {" OR ".join(conditions)}
        """

        cursor.execute(query, values)

        rows = cursor.fetchall()

        return [
            {
                "id_documento": r[0],
                "titulo": r[1],
                "descripcion": r[2]
            }
            for r in rows
        ]