from abc import ABC, abstractmethod
from typing import List,Optional

from modules.auth.domain.entities.user import User


class AuthRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[User]: pass

    @abstractmethod
    def find_by_email(self, email:str) -> Optional[User]: pass

    @abstractmethod
    def save(self,user:User) -> None :pass
