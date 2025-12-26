from modules.auth.domain.gateway.password_gateway import PasswordGateway


class InMemoryPasswordGateway(PasswordGateway):

    def hash(self, password):
        return f"hashed_password_{password}"