from datetime import datetime

#---------------document_service.py---------------#
#Este documento recibe la instruccion del controller y realiza todas las 
#operaciones logicas.

class DocumentService:

    def __init__(self, repository):
        self.repository = repository


    #---------------Crear documentos---------------#
    #Ruta: /doc/create
    #Método logico para crear un documento.
    def create_document(self, data):

        #Lista de campos requeridos.
        codigo_documento = data.get("codigo_documento")
        titulo = data.get("titulo")
        descripcion = data.get("descripcion")
        id_area = data.get("id_area")
        id_tipo = data.get("id_tipo")
        id_estado = data.get("id_estado")

        required_fields = ["codigo_documento", "titulo", "descripcion", "id_estado", "id_area", "id_tipo"]

        #Verificar si todos los campos requeridos han sido llenados.
        if any(data.get(field) is None for field in required_fields):
            return {
                "success": False,
                "message": "Faltan campos requeridos"
            }

        #Regresar valores registrados.
        self.repository.create(
            codigo_documento,
            titulo,
            descripcion,
            id_area,
            id_tipo,
            id_estado
        )

        return {
            "success": True,
            "message": "Documento creado correctamente",
            "data": {
                "codigo_documento": codigo_documento,
                "titulo": titulo,
                "descripcion": descripcion,
                "id_area": id_area,
                "id_tipo": id_tipo,
                "id_estado": id_estado
            }
        }
    
    
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
        
    
    #---------------Actualizar documentos---------------#
    #Ruta: /doc/view/id_documento/update
    #Método logico para actualizar documento por id.
    def update_by_id(self, id_documento, data):
        #Buscar documento actual.
        document = self.repository.get_editable(id_documento=id_documento)

        #Valida si existe el documento.
        if not document:
            return {
                "success": False,
                "message": "Documento no encontrado"
            }

        #Guardar versión anterior.
        self.repository.save_old_version(document)

        #Detectar si es actualización mayor (1.0, 2.0, 3.0, 4.0).
        major_update = data.get("major_update", False)

        #Generar nueva versión (por default es menor (1.1, 1.2, 1.3, 1.4)).
        new_version = self.increase_version(
            document["version_actual"],
            major_update
        )

        #Actualizar documento principal.
        update_by_id = self.repository.update_by_id(
            id_documento,
            data,
            new_version
        )

        return {
            "success": True,
            "message": "Documento actualizado",
            "data": update_by_id
        }
        
    #Ruta: /doc/view/codigo_documento/update
    #Método logico para actualizar documento por codigo.
    def update_by_cod(self, codigo_documento, data):
        #Buscar documento actual.
        document = self.repository.get_editable(codigo_documento=codigo_documento)

        #Valida si existe el documento.
        if not document:
            return {
                "success": False,
                "message": "Documento no encontrado"
            }

        #Guardar versión anterior.
        self.repository.save_old_version(document)

        #Detectar si es actualización mayor (1.0, 2.0, 3.0, 4.0).
        major_update = data.get("major_update", False)

        #Generar nueva versión (por default es menor (1.1, 1.2, 1.3, 1.4)).
        new_version = self.increase_version(
            document["version_actual"],
            major_update
        )

        #Actualizar documento principal.
        update_by_cod = self.repository.update_by_cod(
            codigo_documento,
            data,
            new_version
        )

        return {
            "success": True,
            "message": "Documento actualizado",
            "data": update_by_cod
        }
    
    
    #---------------Version de documentos---------------#
    #Método para aumentar version - Usada en update_by_id y update_by_cod.
    def increase_version(self, current_version, major_update=False):
        #Separar version mayor (1.0 -> 2.0) de versiones menores (1.0 -> 1.1)
        major, minor = map(int, current_version.split("."))

        #Valida si es una version mayor o menor y le aumenta 1
        if major_update:
            major += 1
            minor = 0
        else:
            minor += 1

        return f"{major}.{minor}"
    
    
    #---------------Eliminar documentos---------------#            
    #Método para eliminar documento dependiendo del tiempo (Soft delete mayor a 36 horas o Hard delete menor a 36 horas)
    def delete_by_id(self, id_documento):
        #Buscar documento.
        document = self.repository.get_by_id(
            id_documento
        )

        if not document:
            return {
                "success": False,
                "message": "Documento no encontrado"
            }

        #Fecha creación documento.
        fecha_creacion = document["fecha_creacion"]
        #Fecha actual.
        now = datetime.now()

        #Diferencia horas.
        hours_difference = (now - fecha_creacion).total_seconds() / 3600

        #Llamar Hard delete en caso de ser menor o igual a 36 horas.
        if hours_difference <= 36:
            return self.harddelete_by_id(id_documento)

        #Llamar Soft delete en caso de ser mayor a 36 horas.
        self.repository.soft_delete(id_documento)

        return {
            "success": True,
            "message": "Documento desactivado logicamente"
        }
        
    #Método para eliminar un documento de manera permanente (Hard delete)
    def harddelete_by_id(self, id_documento):

        self.repository.harddelete_by_id(id_documento)

        return {
            "success": True,
            "message": "Documento eliminado completamente"
        }
        
    def restore_document(self, id_documento):

        document = self.repository.get_editable(id_documento)

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
    