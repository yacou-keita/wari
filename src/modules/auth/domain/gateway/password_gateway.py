
from abc import ABC


class PasswordGateway(ABC):

    def hash(password:str) -> str:pass