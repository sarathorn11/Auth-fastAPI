from .. import schema
from sqlalchemy.orm import Session
from ... import models

# sarath 12.05.2023 register
def create_blogs(request:schema.Blog, db:Session):
    new = models.Blog(title=request.title,body=request.body,user_id= 1)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new