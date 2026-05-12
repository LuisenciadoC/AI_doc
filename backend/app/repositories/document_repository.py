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
        SELECT * FROM Documento
        WHERE id_estado = 3
        """
        #actualizar estado aprobado es el valido
        cursor.execute(query)
        rows = cursor.fetchall()

        return [
            {
                "id_documento": r[0],
                "codigo_documento": r[1],
                "titulo": r[2],
                "descripcion": r[3],
                "fecha_creacion": r[4],
                "fecha_actualizacion": r[5],
                "id_area": r[6],
                "id_tipo": r[7]
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
                "id_tipo": row[6],
                "estado": row[7],

                # NUEVOS CAMPOS
                "numero_version": row[8],
                "es_vigente": row[9]
            }

        return None
    
    # Método para actualizar un documento
    def update(self, id_documento, data, new_version):

        # Obtener documento actual
        current_document = self.get_by_id(id_documento)

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE documento
        SET
            titulo = ?,
            descripcion = ?,
            id_area = ?,
            id_tipo = ?,
            numero_version = ?
        WHERE id_documento = ?
        """

        cursor.execute(
            query,
            (
                # Si no envían titulo, conserva el actual
                data.get(
                    "titulo",
                    current_document["titulo"]
                ),

                # Si no envían descripcion, conserva la actual
                data.get(
                    "descripcion",
                    current_document["descripcion"]
                ),

                # Si no envían area, conserva la actual
                data.get(
                    "id_area",
                    current_document["id_area"]
                ),

                # Si no envían tipo, conserva el actual
                data.get(
                    "id_tipo",
                    current_document["id_tipo"]
                ),

                # Nueva versión automática
                new_version,

                # ID documento
                id_documento
            )
        )

        conn.commit()

        return self.get_by_id(id_documento)
    
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
        SET
            estado = 0,
            es_vigente = 0
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
        
    # Método para guardar versiones antiguas
    def save_old_version(self, document):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO version_documento
        (
            numero_version,
            titulo,
            descripcion,
            codigo_documento,
            fecha_creacion,
            es_vigente,
            estado,
            id_documento
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            query,
            (
                document["numero_version"],
                document["titulo"],
                document["descripcion"],
                document["codigo_documento"],
                document["fecha_creacion"],
                0,
                1,
                document["id_documento"]
            )
        )

        conn.commit()
    
    # Método para obtener ultima version
    def get_last_version(self, id_documento):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT TOP 1 *
        FROM version_documento
        WHERE id_documento = ?
        ORDER BY id_version DESC
        """

        cursor.execute(query, (id_documento,))

        row = cursor.fetchone()

        if row:

            return {
                "id_version": row[0],
                "numero_version": row[1],
                "titulo": row[2],
                "descripcion": row[3],
                "codigo_documento": row[4]
            }

        return None
    
    # Método para restaurar versiones
    def restore_version(self, id_documento, version):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE documento
        SET
            titulo = ?,
            descripcion = ?,
            codigo_documento = ?,
            numero_version = ?
        WHERE id_documento = ?
        """

        cursor.execute(
            query,
            (
                version["titulo"],
                version["descripcion"],
                version["codigo_documento"],
                version["numero_version"],
                id_documento
            )
        )

        conn.commit()
    
    # Método para borrar la ultima version    
    def delete_last_version(self, id_version):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM version_documento
        WHERE id_version = ?
        """

        cursor.execute(query, (id_version,))

        conn.commit()
        
    def restore_document(self, id_documento):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE documento
        SET
            estado = 1,
            es_vigente = 1
        WHERE id_documento = ?
        """

        cursor.execute(query, (id_documento,))

        conn.commit()