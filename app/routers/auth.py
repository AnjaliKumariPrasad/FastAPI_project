from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..dependencies import get_db

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):

  user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

  if not user: 
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")          
  if not user.verify(user_credentials.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")     

  access_token = oauth2.create_access_token(data={"user_id": user.id})

  return {"access_token": access_token, "token_type": "bearer" }  
  
