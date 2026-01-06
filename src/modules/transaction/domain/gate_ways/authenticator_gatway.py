from abc import ABC,abstractmethod
from typing import Optional

from src.modules.auth.domain.entities.user import User


class AuthenticatorGatway(ABC):

    @abstractmethod
    def authenticate(self, user:Optional[User]) -> None: pass

    @abstractmethod
    def current_user(self) -> Optional[User]: pass