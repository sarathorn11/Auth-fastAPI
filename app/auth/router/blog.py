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


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog)
def get_blog(id:int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):

    return blog.get_blog(id, db)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id:int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):

    return blog.delete_blog(id, db)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id:int,request: schema.Blog, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):

    return blog.update_blog(id, request, db)

