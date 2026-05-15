from typing import Optional

from pydantic import BaseModel, EmailStr, conint
from datetime import datetime 



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass  
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = {
    "from_attributes": True
}

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = {
    "from_attributes": True
}

class PostOut(BaseModel):
    Post: Post
    votes: int
     
    class Config:
        orm_mode = True 

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None        
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)