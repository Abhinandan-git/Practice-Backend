from fastapi import FastAPI

import src.auth.auth as authenticator
import src.auth.model as models
from src.database.core import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(authenticator.router)
