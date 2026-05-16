from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController

user = Blueprint('user', __name__)

# Crear usuario
@user.route('/create', methods=['POST'])
def create_user():
    data = request.json
    result = UserController.create_user(data)
    return jsonify(result)