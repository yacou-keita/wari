from typing import Optional
from uuid import UUID, uuid4

from src.modules.auth.domain.entities.owner import Owner
from datetime import datetime

from src.modules.transaction.domain.entities.balance import Balance


class TransactionAccount:

    @property
    def id(self) -> UUID: return self.__id

    def __init__(self,
                 id:UUID,
                phone_number:str,
                balance:Balance,
                create_at:datetime,
                owner:Optional[Owner] = None,
                update_at:Optional[datetime] = None
                ) -> None:
        self.__id = id
        self.__phone_number= phone_number
        self.__balance= balance
        self.__owner= owner
        self.__create_at =create_at
        self.__update_at = update_at

    @staticmethod
    def create(
                id:UUID,
                phone_number:str,
                balance:Balance,
                create_at:datetime
    ) -> "TransactionAccount":
        return TransactionAccount(
            id= id,
            balance= balance,
            phone_number=phone_number,
            create_at= create_at)
    
    def add_owner(self,owner:Owner) -> None:
        self.__owner = owner

    def __repr__(self) -> str:
        return f"""
        id:{self.__id}, phone_number:{self.__phone_number},
        balance:{self.__balance}, owner:{self.__owner},
        create_at:{self.__create_at},create_at:{self.__update_at},
        """
        