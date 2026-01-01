from unittest import TestCase, main


from core.domain.exceptions.email_already_exsists import EmailAlreadyExists
from modules.auth.data_source.in_momery.gateway.password_gateway import InMemoryPasswordGateway
from modules.auth.data_source.in_momery.in_memory_auth_repository import InMemoryAuthRepository
from modules.auth.domain.entities.user import User
from modules.auth.domain.gateway.password_gateway import PasswordGateway
from modules.auth.domain.repositories.auth_repository import AuthRepository
from src.modules.auth.domain.features.register.register import Register

class TestRegister(TestCase):

    def setUp(self):
        self.auth_repository:AuthRepository = InMemoryAuthRepository()
        self.password_gateway:PasswordGateway = InMemoryPasswordGateway()
        self.register = Register(
            repository=self.auth_repository,
            password_gateway=self.password_gateway)
        self.yacoukeita = User.create(
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="1234",)

    def test_should_save_user_in_database(self):

        self.register(self.yacoukeita)
        users = self.auth_repository.find_all()
        self.assertIn(self.yacoukeita, users)

    def test_should_fail_to_save_user_when_email_already_exists_in_database(self):
    
        self.register(self.yacoukeita)

        with self.assertRaises(EmailAlreadyExists):
            self.register(self.yacoukeita)

    def test_should_hashed_user_password(self):
        self.register(self.yacoukeita)
        user = self.auth_repository.find_by_email(self.yacoukeita.get_email)
        if user is not None:
            self.assertEqual(user.get_password,"hashed::1234")
        








if __name__ == "__main__":
    main()