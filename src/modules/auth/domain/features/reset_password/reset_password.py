from src.core.domain.exceptions.user_not_found import UserNotFound
from src.modules.auth.domain.features.reset_password.reset_password_request import ResetPasswordRequest
from src.modules.auth.domain.gateway.password_gateway import PasswordGateway
from src.modules.auth.domain.repositories.auth_repository import AuthRepository


class ResetPassword():

    def __init__(self,
                 repository:AuthRepository,
                 password_gateway:PasswordGateway
                 ) -> None:
        self.__repository = repository
        self.__password_gateway = password_gateway

    def __call__(self,request:ResetPasswordRequest) -> None:
        user_found = self.__repository.find_by_email(request.email)
        if user_found is None: raise UserNotFound()
        user_found.update_password(self.__password_gateway.hash(request.password))
        