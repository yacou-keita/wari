from fastapi import FastAPI


application = FastAPI()

@application.get("/")
def login():
    return "je fais du fast api"