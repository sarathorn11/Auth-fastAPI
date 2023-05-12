from fastapi import FastAPI
from . models import Base

from .services import db_session, engine
from .auth.router import auth,user,post

db = db_session.session_factory()

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)


