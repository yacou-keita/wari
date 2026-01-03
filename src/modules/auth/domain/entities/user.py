from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


class User:

    def __init__(
            self,id:UUID,
            firstname:str,
            lastname:str,
            email:str,
            password:str,
            create_at:datetime,
            update_at:Optional[datetime]
            ):
        
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__create_at =create_at
        self.__update_at = update_at

    @classmethod
    def create(cls,
            firstname:str,
            lastname:str,
            email:str,
            password:str):
        return User(
            id=uuid4(),
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            create_at=datetime.now(),
            update_at=None)
    
    @property
    def get_id(self) -> UUID: return self.__id
    @property
    def get_email(self) -> str: return self.__email
    @property
    def get_password(self) -> str: return self.__password

    def hash_password(self, password:str) -> None:
        self.__password = password

    def update_password(self, password:str) -> None:
        self.hash_password(password)
        self.__password = password

    def __repr__(self):
        return f"(id:{self.__id}, firstname:{self.__firstname}, lastnamed:{self.__lastname}, email:{self.__email}, create_at:{self.__create_at}, create_at:{self.__update_at}, password:{self.__password})"
        