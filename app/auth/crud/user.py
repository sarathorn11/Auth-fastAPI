
from .. import schema,hashing
from sqlalchemy.orm import Session
from ... import models

# sarath 12.05.2023 register
def create_user(request:schema.User, db:Session):
    new_user = models.User(email=request.email, password=hashing.Hash.bcrypt(request.password),fullname=request.fullname)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
