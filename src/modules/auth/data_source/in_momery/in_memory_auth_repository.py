from modules.auth.domain.entities.user import User
from modules.auth.domain.repositories.auth_repository import AuthRepository


class InMemoryAuthRepository(AuthRepository): 

    def __init__(self):
        self.__users = {}

    def find_all(self):
        return list(self.__users.values())
    
    def find_by_email(self, email):
        user = next(filter(lambda user: user.get_email() == email,self.find_all()),None)
        print(user)
        return user
    
    def save(self, user:User):
        self.__users[user.get_id()] = user


