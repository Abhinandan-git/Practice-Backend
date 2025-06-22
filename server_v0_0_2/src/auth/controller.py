from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.core import get_db
from auth import model, service
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
	username: str
	password: str

class UserInDB(BaseModel):
	id: int
	username: str

class Token(BaseModel):
	access_token: str
	token_type: str

@router.post("/register", response_model=UserInDB)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
	db_user = db.query(model.User).filter(model.User.username == user.username).first()
	if db_user:
		raise HTTPException(status_code=400, detail="Username already registered")
	
	hashed_password = service.get_password_hash(user.password)
	new_user = model.User(username=user.username, hashed_password=hashed_password)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return UserInDB(id=new_user.id, username=new_user.username)

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
	db_user = db.query(model.User).filter(model.User.username == user.username).first()
	if not db_user or not service.verify_password(user.password, db_user.hashed_password):
		raise HTTPException(status_code=401, detail="Incorrect username or password")

	access_token = service.create_access_token(
		data={"sub": db_user.username}
	)
	return {"access_token": access_token, "token_type": "bearer"}
