from datetime import datetime

#---------------document_service.py---------------#
#Este documento recibe la instruccion del controller y realiza todas las 
#operaciones logicas.

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
    
    #---------------Ver documentos---------------#
    #Ruta: /doc/view    
    #Método de respuesta a la consulta de visualizacion de todos los documentos.
    #Este metodo trabaja con get_all() metodo que se encuentra en document.repository.py
    def view_documents(self):
        documents = self.repository.get_all()
        return {
            "success": True,
            "message": "Lista de documentos",
            "data": documents
        }
        
    #Ruta: /doc/view/id_documento
    #Método de respuesta a la consulta de visualizacion de un documento por medio del id.
    #Este metodo trabaja con get_by_id() metodo que se encuentra en document.repository.py
    def view_documents_id(self, id_documento):
        document = self.repository.get_by_id(id_documento)
        
        #Retorno de informacion.
        return {
            "success": True,
            "data": document
        }
        
    #Ruta: /doc/view/codigo_documento
    #Método de respuesta a la consulta de visualizacion de un documento por medio del codigo.
    #Este metodo trabaja con get_by_cod() metodo que se encuentra en document.repository.py
    def view_documents_cod(self, codigo_documento):
        document = self.repository.get_by_cod(codigo_documento)
        
        #Retorno de informacion.
        return {
            "success": True,
            "data": document
        }
        
    # Método para actualizar documento
    def update_document(self, id_documento, data):

        # Buscar documento actual
        document = self.repository.get_by_id(id_documento)

        if not document:

            return {
                "success": False,
                "message": "Documento no encontrado"
            }

        # Guardar versión anterior
        self.repository.save_old_version(document)

        # Nueva versión
        new_version = self.increase_version(
            document["numero_version"]
        )

        # Actualizar documento principal
        updated_document = self.repository.update(
            id_documento,
            data,
            new_version
        )

        return {
            "success": True,
            "message": "Documento actualizado",
            "data": updated_document
        }
      
    # Método para actualizar y comunicarse con SQL
    def update(self, id_documento, data, new_version):

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
                data.get("titulo"),
                data.get("descripcion"),
                data.get("id_area"),
                data.get("id_tipo"),
                new_version,
                id_documento
            )
        )

        conn.commit()

        return self.get_by_id(id_documento)
        
    # Método para eliminar documento
    def delete_document(self, id_documento):

        # Buscar documento
        document = self.repository.get_by_id(
            id_documento
        )

        if not document:

            return {
                "success": False,
                "message": "Documento no encontrado"
            }

        # Fecha creación documento
        fecha_creacion = document["fecha_creacion"]

        # Fecha actual
        now = datetime.now()

        # Diferencia horas
        hours_difference = (
            now - fecha_creacion
        ).total_seconds() / 3600

        # HARD DELETE
        if hours_difference <= 36:

            return self.hard_delete(id_documento)

        # SOFT DELETE
        self.repository.soft_delete(id_documento)

        return {
            "success": True,
            "message": "Documento desactivado logicamente"
        }
        
    # Método para aumentar version
    def increase_version(self, current_version):

        major, minor = current_version.split(".")

        new_minor = int(minor) + 1

        return f"{major}.{new_minor}"
    
    # Método para eliminar un documento de manera permanente
    def hard_delete(self, id_documento):
        # Buscar última versión guardada
        last_version = self.repository.get_last_version(
            id_documento
        )

        # SI EXISTE HISTORIAL
        if last_version:

            # Restaurar esa versión
            self.repository.restore_version(
                id_documento,
                last_version
            )

            # Eliminarla del historial
            self.repository.delete_last_version(
                last_version["id_version"]
            )

            return {
                "success": True,
                "message": "Versión anterior restaurada"
            }

        # SI NO EXISTE HISTORIAL
        self.repository.hard_delete(id_documento)

        return {
            "success": True,
            "message": "Documento eliminado completamente"
        }
        
    def restore_document(self, id_documento):

        document = self.repository.get_by_id(
            id_documento
        )

        if not document:

            return {
                "success": False,
                "message": "Documento no encontrado"
            }

        self.repository.restore_document(
            id_documento
        )

        return {
            "success": True,
            "message": "Documento restaurado"
        }    
    