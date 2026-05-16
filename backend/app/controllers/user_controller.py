from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

repo = UserRepository()

service = UserService(repo)

class UserController:

    @staticmethod
    def create_user(data):
        return service.create_user(data)