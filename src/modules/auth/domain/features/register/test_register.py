from unittest import TestCase, main
from uuid import uuid4
from datetime import datetime

from modules.auth.data_source.in_momery.in_memory_auth_repository import InMemoryAuthRepository
from modules.auth.domain.entities.user import User
from modules.auth.domain.repositories.auth_repository import AuthRepository
from src.modules.auth.domain.features.register.register import Register

class TestRegister(TestCase):

    def setUp(self):
        self.auth_repository:AuthRepository = InMemoryAuthRepository()
        self.register = Register(self.auth_repository)

    def test_registered_user(self):
        user = User(
        id=uuid4(),
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="hashed_password",
        create_at=datetime.now(),
        update_at=datetime.now())

        self.register(user)

        users = self.auth_repository.find_all()

        self.assertIn(user, users)

        






if __name__ == "__main__":
    main()