from abc import ABC,abstractmethod

from src.modules.auth.domain.entities.user import User




class TokenGateway(ABC):

    @abstractmethod
    def generate(self, user:User) -> str: pass