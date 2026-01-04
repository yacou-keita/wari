from src.modules.auth.domain.entities.user import User


class UserInMemory:

    @staticmethod
    def yacoukeita():
        return User.create(
        firstname="Yacou",
        lastname="Keita",
        email="yacou.keita@mail.com",
        password="1234")
    
    @staticmethod
    def badEmail(): return  "test.keita@mail.com"

    @staticmethod
    def passwordHashed(password:str): return  f"hashed::{password}"

    @staticmethod
    def goodPassword(): return  "1234"
    
    @staticmethod
    def badPassword(): return  "test12"

    @staticmethod
    def updatePassword(): return  "update1234"