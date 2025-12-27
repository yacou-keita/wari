class CredentialRequest:

    def __init__(self,email:str,password:str):
        self.email = email
        self.password = password

    @classmethod
    def create(cls,email:str,password:str):
        return CredentialRequest(email=email,password=password)