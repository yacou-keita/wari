from datetime import datetime
import uuid


class User:

    def __init__(
            self,id:uuid,
            firstname:str,
            lastname:str,
            email:str,
            password:str,
            create_at:datetime,
            update_at:datetime
            ):
        
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.create_at =create_at
        self.update_at = update_at

    def __repr__(self):
        return f"(id:{self.id}, firstname:{self.firstname}, lastnamed:{self.lastname}, email:{self.email}, create_at:{self.create_at}, create_at:{self.update_at})"
        