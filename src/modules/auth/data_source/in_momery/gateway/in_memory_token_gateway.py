from src.modules.auth.domain.entities.user import User
from src.modules.auth.domain.gateway.token_gateway import TokenGateway


class InMemoryTokenGateway(TokenGateway):

    def generate(self, user: User) -> str:
        return f"Bearer {user.get_email}"
    