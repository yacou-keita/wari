from abc import ABC, abstractmethod

from modules.auth.domain.entities.user import User


class AuthRepository(ABC):

    @abstractmethod
    def find_all(self) -> list[User]: pass

    @abstractmethod
    def find_by_email(self, email:str) -> User | None: pass

    @abstractmethod
    def save(self,user:User) -> None :pass
