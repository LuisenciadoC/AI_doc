from werkzeug.security import check_password_hash

class AuthService:

    def __init__(self, user_repository):

        self.user_repository = user_repository

    def login(self, correo, password):

        # Validar campos vacíos
        if not correo or not password:

            return {
                "success": False,
                "message": "Correo y contraseña son obligatorios"
            }

        # Buscar usuario
        user = self.user_repository.get_by_email(correo)

        # Validar existencia
        if not user:

            return {
                "success": False,
                "message": "Usuario no encontrado"
            }

        # Validar contraseña HASH
        valid_password = check_password_hash(
            user["contrasena"],
            password
        )

        if not valid_password:

            return {
                "success": False,
                "message": "Contraseña incorrecta"
            }

        # Validar estado
        if user["estado"] == 0:

            return {
                "success": False,
                "message": "Usuario desactivado"
            }

        # Login exitoso
        return {
            "success": True,
            "message": "Login exitoso",
            "data": {
                "id_usuario": user["id_usuario"],
                "nombre": user["nombre"],
                "correo": user["correo"],
                "id_rol": user["id_rol"]
            }
        }