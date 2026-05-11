import requests

from app.repositories.document_repository import DocumentRepository

class AIService:

    def __init__(self):
        self.repository = DocumentRepository()
        
    def ask_question(self, question):
        documents = self.repository.search_documents(question)
        
        context = ""
        for doc in documents:

            context += f"""
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
        Responde usando la información de los documentos.
        Si encuentras información relacionada, responde de forma clara y resumida.

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