
from abc import ABC, abstractmethod


class PasswordGateway(ABC):
    
    @abstractmethod
    def hash(self,password:str) -> str: pass

    @abstractmethod
    def is_same(self, hashed:str,plain:str) -> bool: pass