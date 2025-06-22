from src.database.core import Base
from sqlalchemy import Column, String, UUID
from uuid import uuid4

class Users(Base):
	__tablename__ = "users"

	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
	username = Column(String, unique=True)
	hashed_password = Column(String)
