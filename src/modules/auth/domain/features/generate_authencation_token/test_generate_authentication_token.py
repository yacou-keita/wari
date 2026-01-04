from unittest import TestCase, main

from src.core.domain.exceptions.user_not_found import UserNotFound
from src.modules.auth.data_source.in_momery.gateway.in_memory_token_gateway import InMemoryTokenGateway
from src.modules.auth.domain.entities.user import User
from src.modules.auth.domain.features.generate_authencation_token.generate_authencation_token import GenerateAuthenticationToken
from src.modules.auth.domain.gateway.token_gateway import TokenGateway


class TestGenerateAuthenticationToken(TestCase):

    def setUp(self) -> None:
        self.token_gateway:TokenGateway = InMemoryTokenGateway()
        self.generate_authentication_token = GenerateAuthenticationToken(self.token_gateway)
        self.yacoukeita = User.create(
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="1234",)

        self.BAD_EMAIL = "test.keita@mail.com"


    def test_generate_authentication_token_when_user_exists(self):

        token = self.generate_authentication_token(self.yacoukeita)

        self.assertEqual(token, str(self.yacoukeita.get_id))

    def test_generate_authentication_token_failed_when_user_does_not_exists(self):

        with self.assertRaises(UserNotFound):
            self.generate_authentication_token(None)

        




if __name__ == "__main__":
    main()