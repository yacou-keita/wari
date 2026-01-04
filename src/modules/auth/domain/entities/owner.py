from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


class Owner:

    def __init__(
            self,id:UUID,
            firstname:str,
            lastname:str,
            email:str
            ):
        
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        

    @staticmethod
    def create(
            id:UUID,
            firstname:str,
            lastname:str,
            email:str):
        return Owner(
            id=id,
            firstname=firstname,
            lastname=lastname,
            email=email)
        
    def __repr__(self):
        return f"""
        id:{self.__id},
        firstname:{self.__firstname},
        lastnamed:{self.__lastname},
        email:{self.__email},
        """
        