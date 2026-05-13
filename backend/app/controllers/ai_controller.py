from app.services.ai_service import AIService

service = AIService()

class AIController:

    #---------------Preguntar a la IA---------------#
    #Ruta: /ai/ask
    #Método estatico para manejar las solicitudes de visualización y actualizacion por 
    #id del frontend. Las respuestas se esperan del archivo document_service.py    
    @staticmethod
    def ask_question(data):
        question = data.get("question")
        return service.ask_question(question)