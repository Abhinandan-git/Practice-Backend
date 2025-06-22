from fastapi import FastAPI
from src.database.core import engine, Base
from auth import model
from auth.controller import router as auth_router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
