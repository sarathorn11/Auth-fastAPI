from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from .services import Base


    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    fullname = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String,default='1')
    
    
