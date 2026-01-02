from abc import ABC, abstractmethod

from src.modules.auth.domain.entities.user import User


class EmailGateway(ABC):

    @abstractmethod
    def send(self,user:User) -> None: pass