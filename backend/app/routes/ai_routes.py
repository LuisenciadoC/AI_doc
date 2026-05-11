from flask import Blueprint, request, jsonify

from app.controllers.ai_controller import AIController

ai = Blueprint('ai', __name__)

@ai.route('/question', methods=['POST'])
def ask_question():
    data = request.json
    result = AIController.ask_question(data)
    return jsonify(result)