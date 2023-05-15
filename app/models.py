from sqlalchemy import Column, DateTime, Integer, String,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .services import Base



class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates='blogs')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    fullname = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String,default='1')
    blogs = relationship("Blog", back_populates='creator')

    
