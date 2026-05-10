from flask import Blueprint, jsonify, request
# Blueprint: permite crear módulos de rutas en Flask
# request: permite recibir datos del cliente (frontend o Thunder Client)
# jsonify: convierte diccionarios a JSON válido

from app.controllers.auth_controller import AuthController
# Importamos el controlador que maneja la lógica de autenticación

auth = Blueprint('auth', __name__)

# Definimos la ruta /login que acepta POST
@auth.route('/login', methods=['POST'])

#Funcion para el login de los usuarios
def login():
    data = request.json
    result = AuthController.login(data)
    return jsonify(result)