from unittest import TestCase, main

from src.core.data_source.in_memory.entities_initialization.user_in_memory import UserInMemory
from src.core.domain.exceptions.user_not_found import UserNotFound
from src.modules.auth.data_source.in_momery.gateway.In_memory_email_gateway import InMemoryEmailGateway
from src.modules.auth.data_source.in_momery.gateway.password_gateway import InMemoryPasswordGateway
from src.modules.auth.data_source.in_momery.in_memory_auth_repository import InMemoryAuthRepository
from src.modules.auth.domain.features.send_reset_password_link.send_reset_password_link import SendResetPasswordLink
from src.modules.auth.domain.features.register.register import Register
from src.modules.auth.domain.gateway.email_gateway import EmailGateway
from src.modules.auth.domain.gateway.password_gateway import PasswordGateway
from src.modules.auth.domain.repositories.auth_repository import AuthRepository


class TestSendResetPasswordLink(TestCase):

    def setUp(self) -> None:
        self.auth_repository:AuthRepository = InMemoryAuthRepository()
        self.password_gateway:PasswordGateway = InMemoryPasswordGateway()
        self.email_gateway:EmailGateway = InMemoryEmailGateway()

        self.register:Register = Register(
            repository=self.auth_repository,
            password_gateway= self.password_gateway
            )
        self.send_reset_password_link:SendResetPasswordLink = SendResetPasswordLink(
            email_gateway=self.email_gateway,
            repository= self.auth_repository
        )

        self.yacoukeita = UserInMemory.yacoukeita()

        self.BAD_EMAIL = UserInMemory.badEmail()
        
        self.register(self.yacoukeita)


    def test_send_reset_password_link__to_user_by_email(self):

        self.send_reset_password_link(self.yacoukeita.get_email)

        users = InMemoryEmailGateway.users

        self.assertIn(self.yacoukeita, list(users.values()))

    def test_fail_sending_reset_password_link_when_user_does_not_exist(self):

        with self.assertRaises(UserNotFound):
            self.send_reset_password_link(self.BAD_EMAIL)

        





if __name__ == "__main__":
    main()