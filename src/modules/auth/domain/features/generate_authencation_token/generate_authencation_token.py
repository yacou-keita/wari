

from typing import Optional
from src.core.domain.exceptions.user_not_found import UserNotFound
from src.modules.auth.domain.entities.user import User
from src.modules.auth.domain.gateway.token_gateway import TokenGateway

class GenerateAuthenticationToken():

    def __init__(self,token_gateway:TokenGateway) -> None:
        self.token_gateway = token_gateway

    def __call__(self,user:Optional[User]) -> str:
       if user is None: raise UserNotFound()
       return self.token_gateway.generate(user)