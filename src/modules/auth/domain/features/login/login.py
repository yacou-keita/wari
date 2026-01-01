from core.domain.exceptions.user_not_found import UserNotFound
from modules.auth.domain.features.login.credential_request import CredentialRequest
from modules.auth.domain.repositories.auth_repository import AuthRepository
from src.modules.auth.domain.gateway.password_gateway import PasswordGateway


class Login:

    def __init__(self, repository:AuthRepository,password_gateway:PasswordGateway):
        self.__repository = repository
        self.__password_gateway = password_gateway

    def __call__(self,credential_request:CredentialRequest):
        user_found = self.__repository.find_by_email(credential_request.email)
        if user_found is None: raise UserNotFound()
        if self.__password_gateway.is_same(
            hashed = user_found.get_password,
            plain = credential_request.password): return user_found 
        raise UserNotFound()
    
        
        
