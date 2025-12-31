
from src.modules.auth.presentation.controllers.auth_controller import auth_router

@auth_router.post("/login")
def login():
    return "je fais du fast api"


@auth_router.post("user/{iban}")
def login(iban):
    return f"je fais du fast api {iban}"