from datetime import datetime
import uuid


class User:

    def __init__(
            self,id:uuid,
            firstname:str,
            lastname:str,
            email:str,
            password:str,
            create_at:datetime,
            update_at:datetime
            ):
        
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__create_at =create_at
        self.__update_at = update_at

    @classmethod
    def create(self,
            firstname:str,
            lastname:str,
            email:str,
            password:str):
        return User(
            id=uuid.uuid4(),
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            create_at=datetime.now(),
            update_at=None)
    
 
    def get_id(self): return self.__id
    def get_email(self): return self.__email
    def get_password(self): return self.__password

    def hash_password(self, password:str) -> None:
        self.__password = password

    def __repr__(self):
        return f"(id:{self.__id}, firstname:{self.__firstname}, lastnamed:{self.__lastname}, email:{self.__email}, create_at:{self.__create_at}, create_at:{self.__update_at})"
        