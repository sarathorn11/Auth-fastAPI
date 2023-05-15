from fastapi import APIRouter, Depends,HTTPException, Request, status
from sqlalchemy.orm import Session

from ..crud import user
from .. import schema
from ... import models
from ..crud import oauth2
from ...utils import database

router = APIRouter()

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

# sarath 12.05.2023- get all users
@router.get("/")
def get_user(db: Session = Depends(database.get_db)):
    return db.query(models.User).all()

# sarath 12.05.2023- create new user
@router.post("/")
def create_new_user(request: schema.User,db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):    
    # create a new user
    return user.create_user(request, db)