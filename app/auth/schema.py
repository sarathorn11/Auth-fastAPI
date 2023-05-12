from pydantic import BaseModel ,Field

class User(BaseModel):
    email:str
    password:str
    fullname:str
    
class Post(BaseModel):
    title:str
    description:str