from unittest import TestCase

from src.modules.auth.data_source.in_momery.gateway.password_gateway import InMemoryPasswordGateway
from src.modules.auth.data_source.in_momery.in_memory_auth_repository import InMemoryAuthRepository
from src.modules.auth.domain.entities.user import User
from src.modules.auth.domain.features.register.register import Register
from src.modules.auth.domain.features.reset_password.reset_password import ResetPassword
from src.modules.auth.domain.features.reset_password.reset_password_request import ResetPasswordRequest
from src.modules.auth.domain.gateway.password_gateway import PasswordGateway
from src.modules.auth.domain.repositories.auth_repository import AuthRepository


class TestResetPassword(TestCase):

    def setUp(self) -> None:
        
        self.auth_repository:AuthRepository = InMemoryAuthRepository()
        self.password_gateway:PasswordGateway = InMemoryPasswordGateway()
        
        self.register:Register = Register(
            repository=self.auth_repository,
            password_gateway= self.password_gateway
            )
  
        self.yacoukeita = User.create(
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="1234",)

        self.BAD_EMAIL = "test.keita@mail.com"
        
        self.register(self.yacoukeita)
        self.reset_password:ResetPassword = ResetPassword()


    def test_reset_password_with_valid_parameters(self):

        self.reset_password(ResetPasswordRequest.create(
            email=self.yacoukeita.get_email,
            password="update1234",
            confirm_password="update1234"))