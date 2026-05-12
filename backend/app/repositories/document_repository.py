from app.config.db import get_connection

#---------------document_repository.py---------------#
#Este documento es el encargado de comunicarse con la base de datos para ejecutar
# instrucciones del service.

class DocumentRepository:

    from app.config.db import get_connection

    def __init__(self):
        # Simulación temporal (hasta conectar SQL Server)
        self.documents = []
        self.versions = []

    #---------------Crear documentos---------------#
    #Ruta: /doc/create 
    #Método para crear documentos en la base de datos mediante query.
    def create(self, codigo_documento, titulo, descripcion, id_area, id_tipo, id_estado):
        #Conexion a la bd.
        conn = get_connection()
        cursor = conn.cursor()

        #Query a ejecutar en la bd para insertar el documento a crear.
        query = """
        INSERT INTO documento (codigo_documento, titulo, descripcion, id_area, id_tipo, id_estado)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        #Ejecutar query.
        cursor.execute(query, (codigo_documento, titulo, descripcion, id_area, id_tipo, id_estado))
        conn.commit()

        #Retornar el documento creado.
        return {
            "codigo_documento": codigo_documento,
            "titulo": titulo,
            "descripcion": descripcion,
            "id_area": id_area,
            "id_tipo": id_tipo,
            "id_estado": id_estado
        }
    
    
    #---------------Ver documentos---------------#
    #Ruta: /doc/view 
    #Método para obtener todos los documentos por estado mediante la base de datos.
    def get_all(self):
        #Conexion a la bd.
        conn = get_connection()
        cursor = conn.cursor()

        #Query a ejecutar en la bd, id_estado = 3 (el numero 3 indica que 
        #muestre solo los que tienen estado aprobado).
        query = """
        SELECT * FROM Documento
        WHERE id_estado = 3
        """
        
        #Ejecutor del query y lista de documentos.
        cursor.execute(query)
        rows = cursor.fetchall()

        #Retornar la informacion obtenida el query con todos los documentos 
        #con estado aprobado en la bd.
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
    
    #Método para obtener todos los documentos por id y estado mediante la base de datos.
    def get_by_id(self, id_documento):
        #Conexion a la bd.
        conn = get_connection()
        cursor = conn.cursor()

        #Query a ejecutar en la bd:
        #id_documento = ? (Inserta el codigo como una consulta y no como un codigo, seguridad contra sql inyection).
        #id_estado = 3 (el numero 3 indica que muestre solo los que tienen estado aprobado).
        query = """
        SELECT * FROM documento 
        WHERE id_documento = ? 
        AND id_estado = 3
        """
        
        #Ejecutor del query y guarda documento.
        cursor.execute(query, (id_documento,))
        r = cursor.fetchone()
        
        #Devolver documento si es encontrado.
        if r:
            return {
                "id_documento": r[0],
                "titulo": r[1],
                "descripcion": r[2],
                "codigo_documento": r[3],
                "fecha_creacion": r[4],
                "id_area": r[5],
                "id_tipo": r[6],
                "fecha_actualizacion": r[7],
                "id_estado": r[8],
                "version_actual": r[9]
            }
        
        #Respuesta si no existe el documento.
        return {
            "success": False,
            "message": "Documento no encontrado"
        }
    
    #Método para obtener todos los documentos por codigo y estado mediante la base de datos.
    def get_by_cod(self, codigo_documento):
        #Conexion a la bd.
        conn = get_connection()
        cursor = conn.cursor()

        #Query a ejecutar en la bd:
        #codigo_documento = ? (Inserta el codigo como una consulta y no como un codigo, seguridad contra sql inyection).
        #id_estado = 3 (el numero 3 indica que muestre solo los que tienen estado aprobado).
        query = """
        SELECT * FROM documento 
        WHERE codigo_documento = ? 
        AND id_estado = 3
        """
        
        #Ejecutor del query y guarda documento.
        cursor.execute(query, (codigo_documento,))
        r = cursor.fetchone()
        
        #Devolver documento si es encontrado.
        if r:

            return {
                "id_documento": r[0],
                "titulo": r[1],
                "descripcion": r[2],
                "codigo_documento": r[3],
                "fecha_creacion": r[4],
                "id_area": r[5],
                "id_tipo": r[6],
                "fecha_actualizacion": r[7],
                "id_estado": r[8],
                "version_actual": r[9]
            }
        
        #Respuesta si no existe el documento.
        return {
            "success": False,
            "message": "Documento no encontrado"
        }
    
    
    #---------------Actualizar documentos---------------#
    #Ruta: /doc/view/id_documento/update
    #Método para obtener los documentos editables.
    def get_editable(self, id_documento=None, codigo_documento=None):
        conn = get_connection()
        cursor = conn.cursor()

        if id_documento is not None:
            query = "SELECT * FROM documento WHERE id_documento = ?"
            cursor.execute(query, (id_documento,))
        elif codigo_documento is not None:
            query = "SELECT * FROM documento WHERE codigo_documento = ?"
            cursor.execute(query, (codigo_documento,))
        else:
            return None

        r = cursor.fetchone()

        if r:
            return {
                "id_documento": r[0],
                "titulo": r[1],
                "descripcion": r[2],
                "codigo_documento": r[3],
                "fecha_creacion": r[4],
                "id_area": r[5],
                "id_tipo": r[6],
                "fecha_actualizacion": r[7],
                "id_estado": r[8],
                "version_actual": r[9]
            }
        else:
            return {
                "success": False,
                "message": "Documento no encontrado"
            }

    
    #Método para actualizar un documento por id. 
    def update_by_id(self, id_documento, data, new_version):
        #Obtener documento actual.
        current_document = self.get_editable(id_documento)

        #Conexion a la bd y consulta.
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Documento SET
            titulo = ?,
            descripcion = ?,
            id_area = ?,
            id_tipo = ?,
            version_actual = ?,
            id_estado = ?,
            fecha_actualizacion = GETDATE()
        WHERE id_documento = ?
        """

        cursor.execute(query, (
            data.get("titulo", current_document["titulo"]),
            data.get("descripcion", current_document["descripcion"]),
            data.get("id_area", current_document["id_area"]),
            data.get("id_tipo", current_document["id_tipo"]),
            new_version,
            data.get("id_estado", 1),
            id_documento)
        )

        conn.commit()

        return self.get_editable(id_documento)
    
    #Método para actualizar un documento por codigo. 
    def update_by_cod(self, codigo_documento, data, new_version):
        #Obtener documento actual.
        current_document = self.get_editable(codigo_documento=codigo_documento)

        #Conexion a la bd y consulta.
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Documento SET
            titulo = ?,
            descripcion = ?,
            id_area = ?,
            id_tipo = ?,
            version_actual = ?,
            id_estado = ?,
            fecha_actualizacion = GETDATE()
        WHERE codigo_documento = ?
        """

        cursor.execute(query, (
            data.get("titulo", current_document["titulo"]),
            data.get("descripcion", current_document["descripcion"]),
            data.get("id_area", current_document["id_area"]),
            data.get("id_tipo", current_document["id_tipo"]),
            new_version,
            data.get("id_estado", 1),
            codigo_documento)
        )

        conn.commit()

        return self.get_editable(codigo_documento=codigo_documento)

    
    
    #---------------Version de documentos---------------#
    #Método para guardar versiones antiguas
    def save_old_version(self, document):
        #Conexion a la bd.
        conn = get_connection()
        cursor = conn.cursor()
        
        #Consulta para guardar documento como snapshot en tabla version_documento.
        query = """
        INSERT INTO version_documento
        (
            id_documento,
            titulo,
            descripcion,
            codigo_documento,
            fecha_creacion,
            id_area,
            id_tipo,
            fecha_actualizacion,
            id_estado,
            version_actual
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            query,
            (
                document["id_documento"],
                document["titulo"],
                document["descripcion"],
                document["codigo_documento"],
                document["fecha_creacion"],
                document["id_area"],
                document["id_tipo"],
                document["fecha_actualizacion"],
                document["id_estado"],
                document["version_actual"]
            )
        )

        conn.commit()
    
        
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