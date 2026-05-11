from app.services.ai_service import AIService

service = AIService()

class AIController:

    @staticmethod
    def ask_question(data):
        question = data.get("question")
        return service.ask_question(question)