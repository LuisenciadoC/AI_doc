from multiprocessing import connection
from webbrowser import get

from flask import Blueprint, request
#Blueprint para las rutas de autenticación
#request para obtener los datos enviados por el cliente

from app.config.db import get_connection
#Importamos la función para obtener la conexión a la base de datos

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])

#Funcion para el login de los usuarios
def login():
    data = request.json
    correo = data.get('correo')
    password = data.get('password')

    try:
        connection = get_connection()
        #Conección a la base de datos
        
        cursor = connection.cursor()
        #Ejecuta consultas a la base de datos
        
        query = """
            SELECT * FROM usuarios 
            WHERE correo = ? AND password = ?
        """
        #Seguridad a la hora de tomar los datos del usuario para evitar 
        #inyecciones SQL (el ? toma los valores literales y no como codigo)
        
        cursor.execute(query, (correo, password))
        
        user = cursor.fetchone()
        #Obtiene el primer resultado de la consulta de lo contrario devuelve none
        
        #Validamos si el usuario existe
        if user:
            return {
                "success": True,
                "message": "Login exitoso",
            }
    
    except Exception as e:
        return {
            "success": False,
            "message": str(e),
        }
        
    if __name__ == '__main__':
        auth.run(debug=True)