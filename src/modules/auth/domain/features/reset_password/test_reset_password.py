from unittest import TestCase

from src.core.domain.exceptions.user_not_found import UserNotFound
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
        self.UPDATE_PASSWORD = "update1234"
        
        self.register(self.yacoukeita)
        self.reset_password:ResetPassword = ResetPassword(
            repository=self.auth_repository,
            password_gateway= self.password_gateway
            )


    def test_reset_password_with_valid_parameters(self):

        self.reset_password(ResetPasswordRequest.create(
            email=self.yacoukeita.get_email,
            password=self.UPDATE_PASSWORD,
            confirm_password=self.UPDATE_PASSWORD))
        
        user = self.auth_repository.find_by_email(self.yacoukeita.get_email)
        if user is not None:
            self.assertEqual(user.get_password,f"hashed::{self.UPDATE_PASSWORD}")

    def test_failed_to_reset_password_when_user_does_not_exits(self):
        request = ResetPasswordRequest.create(
            email=self.BAD_EMAIL,
            password=self.UPDATE_PASSWORD,
            confirm_password=self.UPDATE_PASSWORD)
        
        with self.assertRaises(UserNotFound):
            self.reset_password(request)
