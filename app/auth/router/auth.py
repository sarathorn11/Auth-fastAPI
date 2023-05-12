from fastapi import APIRouter, Depends,HTTPException, status,Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from ...utils import database
from ..crud import token




router = APIRouter()

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/login')
def login(response: Response,request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    return token.user_login(response,request,db)
