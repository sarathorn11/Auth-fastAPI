from pydantic import BaseModel ,Field
from typing import List, Optional

class User(BaseModel):
    email:str
    password:str
    fullname:str


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True


class ShowUser(User):
    email:str
    password:str
    fullname:str
    blogs: List['Blog'] = []
    
    class Config():
        orm_mode = True

class ShowBlog(Blog):
    title: str
    body: str
    creator : ShowUser

    class Config:
        orm_mode = True

  
class Login(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    email: Optional[str] = None

