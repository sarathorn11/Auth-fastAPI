from fastapi import APIRouter, Depends,HTTPException, Request, status
from sqlalchemy.orm import Session

from ..crud import user
from .. import schema
from ...utils import database

router = APIRouter()

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post("/register")
def register(request: schema.User,requests:Request, db: Session = Depends(database.get_db)):    
    # create a new user
    return user.create_user(request, db)