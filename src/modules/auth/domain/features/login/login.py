from core.domain.exceptions.user_not_found import UserNotFound
from modules.auth.domain.features.login.credential_request import CredentialRequest
from modules.auth.domain.repositories.auth_repository import AuthRepository


class Login:

    def __init__(self, repository:AuthRepository):
        self.__repository = repository

    def __call__(self,credential_request:CredentialRequest):
        user = self.__repository.find_by_email(credential_request.email)
        if user is None: raise UserNotFound()
        return user