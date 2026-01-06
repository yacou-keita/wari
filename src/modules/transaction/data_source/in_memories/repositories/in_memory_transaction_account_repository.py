
from typing import Dict, List
from uuid import UUID
from src.modules.transaction.domain.entities.transaction_account import TransactionAccount
from src.modules.transaction.domain.repositories.transaction_account_repository import TransactionAccountRepository


class InMemoryTransactionAccountRepository(TransactionAccountRepository):

    def __init__(self) -> None:
        self.__transaction_accounts:Dict[UUID, TransactionAccount] = {}

    def find_all(self) -> List[TransactionAccount]:
        return list(self.__transaction_accounts.values())
    
    def save(self, transaction_account: TransactionAccount) -> None:
        self.__transaction_accounts[transaction_account.id] = transaction_account