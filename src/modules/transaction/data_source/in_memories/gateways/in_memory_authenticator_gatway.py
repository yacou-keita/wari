from typing import Optional
from src.modules.auth.domain.entities.user import User
from src.modules.transaction.domain.gate_ways.authenticator_gatway import AuthenticatorGatway


class InMemoryAuthenticatorGatway(AuthenticatorGatway):

    def __init__(self) -> None:
        self.user_authenticate:Optional[User] = None

    def authenticate(self, user: Optional[User]) -> None:
        self.user_authenticate = user

    def current_user(self) -> Optional[User]:
        return self.user_authenticate