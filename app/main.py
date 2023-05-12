from fastapi import FastAPI
from . models import Base

from .services import db_session, engine
from .auth.router import auth

db = db_session.session_factory()

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(auth.router)


