from pydantic import BaseModel ,Field
from typing import List, Optional

class User(BaseModel):
    email:str
    password:str
    fullname:str
    
class Post(BaseModel):
    title:str
    description:str
    
class Login(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    email: Optional[str] = None

