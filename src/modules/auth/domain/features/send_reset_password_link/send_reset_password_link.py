from typing import Any

from src.core.domain.exceptions.user_not_found import UserNotFound
from src.modules.auth.domain.gateway.email_gateway import EmailGateway
from src.modules.auth.domain.repositories.auth_repository import AuthRepository


class SendResetPasswordLink():

    def __init__(self,email_gateway:EmailGateway,repository:AuthRepository) -> None:
        self.__email_gateway = email_gateway
        self.__repository = repository

    def __call__(self,email:str) -> Any:
        user_found = self.__repository.find_by_email(email)
        if user_found is None: raise UserNotFound()
        self.__email_gateway.send(user_found)