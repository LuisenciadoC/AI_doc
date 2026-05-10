from app.services.auth_service import AuthService
# Service contiene la lógica de negocio (validaciones, reglas)
from app.repositories.user_repository import UserRepository

user_repo = UserRepository()
auth_service = AuthService(user_repo)

class AuthController:

    @staticmethod
    def login(data):

        # Extraemos datos del JSON recibido desde la ruta
        correo = data.get("correo")
        password = data.get("password")
        
        return auth_service.login(correo, password)