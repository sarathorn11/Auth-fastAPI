from fastapi import APIRouter, Depends,HTTPException, Request, status
from sqlalchemy.orm import Session

from ..crud import user
from .. import schema
from ... import models
from ...utils import database

router = APIRouter()

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

# sarath 12.05.2023- get all users
@router.get("/")
def get_user(requests:Request, db: Session = Depends(database.get_db)):
    return db.query(models.User).all()

# sarath 12.05.2023- create new user
@router.post("/")
def create_new_user(request: schema.User,db: Session = Depends(database.get_db)):    
    # create a new user
    return user.create_user(request, db)