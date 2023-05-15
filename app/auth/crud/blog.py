from .. import schema
from sqlalchemy.orm import Session
from ... import models
from fastapi import HTTPException,status

# sarath 12.05.2023 register
def create_blogs(request:schema.Blog, db:Session):
    new = models.Blog(title=request.title,body=request.body,user_id= 1)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_blog(id:int, db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blogs:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"ID {id} NOT FOUND.")

    return blogs

def delete_blog(id:int, db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)

    if not blogs.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"ID {id} is NOT FOUND.")

    blogs.delete(synchronize_session=False)
    db.commit()

    return "DELETED"

def update_blog(id:int, request: schema.Blog, db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)

    if not blogs.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"ID {id} is NOT FOUND.")

    blogs.update(request.dict())
    db.commit()

    return "UPDATED"