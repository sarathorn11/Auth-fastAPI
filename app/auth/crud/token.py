from fastapi import HTTPException, status
from ... import models

from ..hashing import Hash
from ..token import token

  
def user_login(response,request,db):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    # response.set_cookie(key="username", value=user.email)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"USER is NOT FOUND.")

    if not Hash.verify(user.password, request.password):
        print("+++++++++++++++++++++++", Hash.verify(user.password, request.password))
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Incorrect Password.")


    access_token = token.create_access_token(data={"sub": user.email})
    refresh_token = token.create_refresh_token(data={"sub": user.email})

    return {"access_token": access_token,"refresh_token":refresh_token, "token_type": "bearer"}
