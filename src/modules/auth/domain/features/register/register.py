
from modules.auth.domain.entities.user import User
from modules.auth.domain.repositories.auth_repository import AuthRepository


class Register:

    def __init__(self, repository:AuthRepository):
        self.repository = repository

    def __call__(self, user:User):
        self.repository.save(user=user)