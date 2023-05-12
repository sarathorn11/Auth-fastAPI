from fastapi import APIRouter, Depends,HTTPException, Request, status
from sqlalchemy.orm import Session

from ..crud import post
from .. import schema
from ... import models
from ...utils import database

router = APIRouter()

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

# sarath 12.05.2023- get all posts
@router.get("/")
def get_posts(requests:Request, db: Session = Depends(database.get_db)):
    return db.query(models.Post).all()

# sarath 12.05.2023- create new post
@router.post("/")
def create_new_post(request: schema.Post,db: Session = Depends(database.get_db)):    
    # create a new post
    return post.create_posts(request, db)