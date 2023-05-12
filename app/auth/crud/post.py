from .. import schema
from sqlalchemy.orm import Session
from ... import models

# sarath 12.05.2023 register
def create_posts(request:schema.Post, db:Session):
    new_post = models.Post(title=request.title,description=request.description)
    print("+++++++++++++++++++++++",request.title)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post