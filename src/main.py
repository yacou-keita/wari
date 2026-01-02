from fastapi import FastAPI
from src.modules.auth.presentation.controllers.auth_controller import auth_router


application = FastAPI()
api_verion = "/api/v1"


application.include_router(prefix=api_verion,router=auth_router)





