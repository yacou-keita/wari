from abc import ABC, abstractmethod
from typing import List
from src.modules.transaction.domain.entities.transaction_account import TransactionAccount


class TransactionAccountRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[TransactionAccount]: pass

    @abstractmethod
    def save(self,transaction_account:TransactionAccount) -> None: pass