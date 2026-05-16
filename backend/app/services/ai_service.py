import requests
from app.repositories.document_repository import DocumentRepository

#---------------ai_service.py---------------#
#Este documento recibe la instruccion del controller y realiza todas las 
#operaciones logicas.

class AIService:

    def __init__(self):
        self.repository = DocumentRepository()
        
    #---------------Preguntar por documentos---------------#
    #Ruta: /ai/ask
    #Método logico para realizar preguntas a la ia sobre la documentacion.  
    def ask_question(self, question):
        documents = self.repository.search_documents(question)
        
        context = ""
        for doc in documents:

            context += f"""
            Código: {doc['codigo_documento']}
            Título: {doc['titulo']}
            Descripción: {doc['descripcion']}
            """

        if not documents:
            return {
                "success": False,
                "response": "No se encontraron documentos relacionados."
            }
        
        # Prompt enviado a Ollama
        prompt = f"""
        Responde usando la información de los documentos, incluye de manera breve el titulo, el codigo del documento y el resumen o respuesta a la pregunta en tu respuesta..
        Si encuentras información relacionada, responde de forma clara, resumida y directa con un paso a paso y con una respuesta estandar usando el siguiente formato:
        
        Titulo: Titulo de los documentos
        Codigo: codigos de los documentos
        
        Respuesta: Respuesta a la pregunta del usuario
        Pasos a seguir: Paso a paso a seguir para cumplir lo que dice el documento.
        
        Documentos:
        {context}

        Pregunta:
        {question}
        """

        # Request a Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return {
            "success": True, 
            "response": data["response"]
        }
        