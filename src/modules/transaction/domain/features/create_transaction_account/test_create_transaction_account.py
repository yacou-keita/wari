from unittest import TestCase, main

from src.core.data_source.in_memory.entities_initialization.user_in_memory import UserInMemory
from src.modules.transaction.domain.entities.transaction_account import TransactionAccount
from src.modules.transaction.domain.features.create_transaction_account.create_transaction_account import CreateTransactionAccount


class TestCreateTransactionAccount(TestCase):

    def setUp(self) -> None:
        self.create_transaction_account:CreateTransactionAccount = CreateTransactionAccount()

    def test_create_transaction_account_when_request_valid(self):

        user = UserInMemory.yacoukeita()

        self.create_transaction_account(TransactionAccount.create(phone_number="0100000101",owner=user.create_owner()))




if __name__ == "__main__":
    main()