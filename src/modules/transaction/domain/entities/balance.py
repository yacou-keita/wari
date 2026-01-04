from decimal import Decimal


class Balance:
    def __init__(self,amount:Decimal,currency:str) -> None:
        self.__amount = amount
        self.__currency = currency

    @staticmethod
    def init() -> "Balance": return Balance(amount=Decimal(0),currency="cfa")

    def __repr__(self) -> str:
        return f"""
        amount:{self.__amount},
        currency:{self.__currency}
        """