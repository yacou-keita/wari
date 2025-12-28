from unittest import TestCase, main

from core.domain.exceptions.user_not_found import UserNotFound
from modules.auth.data_source.in_momery.gateway.password_gateway import InMemoryPasswordGateway
from modules.auth.data_source.in_momery.in_memory_auth_repository import InMemoryAuthRepository
from modules.auth.domain.entities.user import User
from modules.auth.domain.features.login.credential_request import CredentialRequest
from modules.auth.domain.features.login.login import Login
from modules.auth.domain.features.register.register import Register
from modules.auth.domain.gateway.password_gateway import PasswordGateway
from modules.auth.domain.repositories.auth_repository import AuthRepository

class TestLogin(TestCase):

    def setUp(self):
        self.auth_repository:AuthRepository = InMemoryAuthRepository()
        self.password_gateway:PasswordGateway = InMemoryPasswordGateway()

        self.register:Register = Register(
            repository=self.auth_repository,
            password_gateway= self.password_gateway
            )
        self.login = Login(repository=self.auth_repository)
        self.yacoukeita = User.create(
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="1234",)


    def test_authenticate_user_with_valid_credentials(self):
        self.register(self.yacoukeita)
        user_logged = self.login(CredentialRequest.create(
            email=self.yacoukeita.get_email(),
            password=self.yacoukeita.get_password()
            ))
        
        users = self.auth_repository.find_all()

        self.assertIn(user_logged, users)

    def test_authentication_fails_when_email_is_unknown(self):
        self.register(self.yacoukeita)

        with self.assertRaises(UserNotFound):
            self.login(CredentialRequest.create(
                email="test@gmail",
                password= self.yacoukeita
                ))

    def test_authentication_fails_when_password_is_unknown(self):
        self.register(self.yacoukeita)

        with self.assertRaises(UserNotFound):
            self.login(CredentialRequest.create(
                email= self.yacoukeita.get_email(),
                password= "test12"
                ))

if __name__ == "__main__":
    main()