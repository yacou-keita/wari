from datetime import datetime
from unittest import TestCase, main
from uuid import uuid4

from src.core.data_source.in_memory.entities_initialization.user_in_memory import UserInMemory
from src.modules.transaction.data_source.in_memories.gateways.in_memory_authenticator_gatway import InMemoryAuthenticatorGatway
from src.modules.transaction.data_source.in_memories.repositories.in_memory_transaction_account_repository import InMemoryTransactionAccountRepository
from src.modules.transaction.domain.entities.balance import Balance
from src.modules.transaction.domain.entities.transaction_account import TransactionAccount
from src.modules.transaction.domain.features.create_transaction_account.create_transaction_account import CreateTransactionAccount
from src.modules.transaction.domain.gate_ways.authenticator_gatway import AuthenticatorGatway
from src.modules.transaction.domain.repositories.transaction_account_repository import TransactionAccountRepository


class TestCreateTransactionAccount(TestCase):

    def setUp(self) -> None:
        self.transaction_account_repository:TransactionAccountRepository = InMemoryTransactionAccountRepository()
        self.authenticator_gatway:AuthenticatorGatway = InMemoryAuthenticatorGatway()
        self.create_transaction_account:CreateTransactionAccount = CreateTransactionAccount(
            repository= self.transaction_account_repository,
            authenticator_gatway= self.authenticator_gatway
            )
        self.user = UserInMemory.yacoukeita()

    def test_create_transaction_account_when_user_is_authenticate(self):

        self.authenticator_gatway.authenticate(self.user)
        transaction_account = TransactionAccount.create(id= uuid4(),
                                                        balance= Balance.init(),
                                                        create_at= datetime.now(),
                                                        phone_number="0100000101")
        
        self.create_transaction_account(transaction_account)

        transaction_accounts = self.transaction_account_repository.find_all()

        self.assertIn(transaction_account, transaction_accounts)
        


        
        




if __name__ == "__main__":
    main()