class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, correo, password):
        
        #Validacion de campos vacíos
        if not correo or not password:
            return {
                "success": False,
                "message": "Correo y contraseña son obligatorios"
            }
            
        # Buscamos el usuario en la base de datos
        user = self.user_repository.get_by_email(correo)
        
        # Si no existe el usuario
        if not user:
            return {
                "success": False,
                "message": "Usuario no encontrado"
            }

        # Validación de contraseña (en futuro aquí se usa hash)
        if user["contraseña"] != password:
            return {
                "success": False,
                "message": "Contraseña incorrecta"
            }
            
        # Si todo está bien, devolvemos información del usuario
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