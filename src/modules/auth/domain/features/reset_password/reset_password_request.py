
class ResetPasswordRequest:

    def __init__(self, email:str, password:str,confirm_password:str) -> None:
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    @classmethod
    def create(cls,email:str, password:str,confirm_password:str):
        return ResetPasswordRequest(
            confirm_password=confirm_password,
            email=email,
            password=password)