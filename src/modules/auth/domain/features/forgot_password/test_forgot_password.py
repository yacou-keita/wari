from unittest import TestCase, main

from src.modules.auth.data_source.in_momery.gateway.password_gateway import InMemoryPasswordGateway
from src.modules.auth.data_source.in_momery.in_memory_auth_repository import InMemoryAuthRepository
from src.modules.auth.domain.entities.user import User
from src.modules.auth.domain.features.forgot_password.forgot_password import ForgotPassword
from src.modules.auth.domain.features.register.register import Register
from src.modules.auth.domain.gateway.password_gateway import PasswordGateway
from src.modules.auth.domain.repositories.auth_repository import AuthRepository


class TestForgotPassword(TestCase):

    def setUp(self) -> None:
        self.auth_repository:AuthRepository = InMemoryAuthRepository()
        self.password_gateway:PasswordGateway = InMemoryPasswordGateway()

        self.register:Register = Register(
            repository=self.auth_repository,
            password_gateway= self.password_gateway
            )
        self.forgot_password:ForgotPassword = ForgotPassword()

        self.yacoukeita = User.create(
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="1234",)


    def test_send_reset_password_link__to_user_by_email(self):

        self.register(self.yacoukeita)

        self.forgot_password(self.yacoukeita.get_email)

        





if __name__ == "__main__":
    main()