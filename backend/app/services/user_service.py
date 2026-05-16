from werkzeug.security import generate_password_hash

class UserService:

    def __init__(self, repository):

        self.repository = repository

    # Crear usuario
    def create_user(self, data):
        nombre = data.get("nombre")
        correo = data.get("correo")
        contrasena = data.get("contrasena")
        id_rol = data.get("id_rol")
        required_fields = [
            "nombre",
            "correo",
            "contrasena",
            "id_rol"
        ]

        # Validar campos
        if any(data.get(field) is None for field in required_fields):
            return {
                "success": False,
                "message": "Faltan campos requeridos"
            }

        #Hash password
        hashed_password = generate_password_hash(
            contrasena
        )

        #Crear usuario
        self.repository.create_user(
            nombre,
            correo,
            hashed_password,
            id_rol
        )

        return {
            "success": True,
            "message": "Usuario creado correctamente"
        }