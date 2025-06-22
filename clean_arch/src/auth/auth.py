from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status
from src.database.core import DatabaseSession
from .model import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import uuid

router = APIRouter(
	prefix="/auth",
	tags=["Authentication"]
)

SECRET_KEY = "d0679e4c5bee90cb51808aea9737c1d0e5bd1d4bef77b688fb5f00aa45afc100"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
	username: str
	password: str

class Token(BaseModel):
	access_token: str
	token_type: str

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(database: DatabaseSession, create_user_request: CreateUserRequest):
	create_user_model = Users(
		id = uuid.uuid4(),
		username = create_user_request.username,
		hashed_password = bcrypt_context.hash(create_user_request.password)
	)

	database.add(create_user_model)
	database.commit()
