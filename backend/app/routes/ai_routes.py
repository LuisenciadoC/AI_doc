from flask import Blueprint, request, jsonify
from app.controllers.ai_controller import AIController

#---------------ai_routes.py---------------#
#En este archivo se crean las rutas correspondientes a la IA que 
#reciben peticiones HTTP del usuario.

ai = Blueprint('ai', __name__)

#---------------Preguntar a la IA---------------#
#Ruta: /ai/ask
#Funcion para preguntar a la IA, esta funcion obtiene los resultados del archivo ai_controller.py
#El resultado se convierte en una respuesta tipo Json.
@ai.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    result = AIController.ask_question(data)
    return jsonify(result)
