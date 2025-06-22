from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

DATABASE_URL = "postgresql://postgres:123456789@172.17.0.1:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database():
	database = SessionLocal()
	try:
		yield database
	finally:
		database.close()

DatabaseSession = Annotated[Session, Depends(get_database)]
