from typing import Dict
from uuid import UUID
from src.modules.auth.domain.entities.user import User
from src.modules.auth.domain.gateway.email_gateway import EmailGateway


class InMemoryEmailGateway(EmailGateway):

    users:Dict[UUID,User] = {}

    def send(self, user: User) -> None:
        self.users[user.get_id] = user
