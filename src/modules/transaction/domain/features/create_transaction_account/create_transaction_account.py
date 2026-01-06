

from src.modules.transaction.domain.entities.transaction_account import TransactionAccount
from src.modules.transaction.domain.gate_ways.authenticator_gatway import AuthenticatorGatway
from src.modules.transaction.domain.repositories.transaction_account_repository import TransactionAccountRepository


class CreateTransactionAccount:

    def __init__(self,
                 repository:TransactionAccountRepository,
                 authenticator_gatway:AuthenticatorGatway
                 ) -> None:
        self.__repository = repository
        self.__authenticator_gatway = authenticator_gatway

    def __call__(self,transaction_account:TransactionAccount) -> None:
        user_authenticate = self.__authenticator_gatway.current_user()
        if user_authenticate:
            transaction_account.add_owner(user_authenticate.create_owner())
            self.__repository.save(transaction_account)