from sqlalchemy import Column, String, UUID, ARRAY
from database import Base

class File(Base):
	__tablename__ = "files"

	id = Column(UUID, primary_key=True, index=True)
	code = Column(String, index=False, nullable=True)
	language = Column(String, index=False, nullable=False)
	users = Column(ARRAY(UUID), nullable=False)

class User(Base):
	__tablename__ = "users"

	id = Column(UUID, primary_key=True, index = True)
	username = Column(String, nullable=False, unique=True)
	files = Column(ARRAY(UUID), nullable=True)
