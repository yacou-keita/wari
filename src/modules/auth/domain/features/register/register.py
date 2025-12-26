
from core.domain.exceptions.email_already_exsists import EmailAlreadyExists
from modules.auth.domain.entities.user import User
from modules.auth.domain.gateway.password_gateway import PasswordGateway
from modules.auth.domain.repositories.auth_repository import AuthRepository


class Register:

    def __init__(
            self,
            repository:AuthRepository,
            password_gateway: PasswordGateway
            ):
        self.__repository = repository
        self.__password_gateway = password_gateway

    def __call__(self, user:User):
        email = user.get_email()
        user_found = self.__repository.find_by_email(email)
        if user_found is not None:
            raise EmailAlreadyExists(email)
        user.hash_password(self.__password_gateway.hash(user.get_password()))
        self.__repository.save(user=user)