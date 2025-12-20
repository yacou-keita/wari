from modules.auth.domain.entities.user import User
from modules.auth.domain.repositories.auth_repository import AuthRepository


class InMemoryAuthRepository(AuthRepository): 
    users = {}

    def find_all(self):
        return list(self.users.values())
    
    def save(self, user:User):
        self.users[user.id] = user