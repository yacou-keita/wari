
from abc import ABC, abstractmethod


class PasswordGateway(ABC):
    
    @abstractmethod
    def hash(self,password:str) -> str: pass