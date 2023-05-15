from fastapi import APIRouter, Depends,HTTPException, Request, status
from sqlalchemy.orm import Session

from ..crud import blog
from .. import schema
from ... import models
from ...utils import database

router = APIRouter()

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

# sarath 12.05.2023- get all posts
@router.get("/")
def get_blogs(db: Session = Depends(database.get_db)):
    return db.query(models.Blog).all()

# sarath 12.05.2023- create new post
@router.post("/")
def create_new_blogs(request: schema.Blog,db: Session = Depends(database.get_db)):    
    # create a new post
    return blog.create_blogs(request, db)