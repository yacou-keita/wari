from modules.auth.domain.gateway.password_gateway import PasswordGateway


class InMemoryPasswordGateway(PasswordGateway):

    def hash(self, password:str):
        return f"hashed::{password}"
    
    def is_same(self, hashed: str, plain: str) -> bool:
        return hashed == f"hashed::{plain}"