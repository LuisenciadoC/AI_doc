from app.services.document_service import DocumentService
from app.repositories.document_repository import DocumentRepository

#---------------document_controller.py---------------#
#En este archivo se reciben las peticiones del usuario por medio de los
#routes y elige la funcion a ejecutar por medio de metodos estaticos.

# Instancias (inyección simple)
repo = DocumentRepository()
service = DocumentService(repo)

class DocumentController:

    #---------------Crear documentos---------------#
    #Ruta: /doc/create
    #Método estático para manejar las solicitudes de creación del frontend.
    #Las respuestas se esperan del archivo document_service.py
    @staticmethod
    def create_document(data):
        return service.create_document(data)
    
    
    #---------------Ver documentos---------------#
    #Ruta: /doc/view    
    #Método estatico para manejar las solicitudes de visualización del frontend.
    #Las respuestas se esperan del archivo document_service.py
    @staticmethod
    def view_documents():
        return service.view_documents()
    
    #Ruta: /doc/view/id_documento 
    #Método estatico para manejar las solicitudes de visualización por id del 
    #frontend. Las respuestas se esperan del archivo document_service.py
    @staticmethod
    def view_document_id(id_documento):
        return service.view_documents_id(id_documento)
    
    #Ruta: /doc/view/codigo_documento 
    #Método estatico para manejar las solicitudes de visualización por codigo del 
    #frontend. Las respuestas se esperan del archivo document_service.py
    @staticmethod
    def view_document_cod(codigo_documento):
        return service.view_documents_cod(codigo_documento)
    
    
    #---------------Actualizar documentos---------------#
    #Ruta: /doc/view/id_documento/update
    #Método estatico para manejar las solicitudes de visualización y actualizacion por 
    #id del frontend. Las respuestas se esperan del archivo document_service.py
    @staticmethod
    def update_by_id(id_documento, data):
        return service.update_by_id(id_documento, data)
    
    #Ruta: /doc/view/codigo_documento/update
    #Método estatico para manejar las solicitudes de visualización y actualizacion por 
    #codigo del frontend. Las respuestas se esperan del archivo document_service.py
    @staticmethod
    def update_by_cod(codigo_documento, data):
        return service.update_by_cod(codigo_documento, data)
    
    
# Métodos para eliminar documento   
    # Método para hacer Soft delete
    @staticmethod
    def delete_document(id_documento):
        return service.delete_document(
            id_documento
        )
    
    # Método para eliminar de manera permanente
    @staticmethod
    def hard_delete(id_documento):
        return service.hard_delete(id_documento)
    
    @staticmethod
    def restore_document(id_documento):

        return service.restore_document(
            id_documento
        )
        
    