from fastapi import FastAPI
from .database import engine
from blogs import models
from .routers import authentication,users

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)