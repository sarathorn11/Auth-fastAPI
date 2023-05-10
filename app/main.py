from fastapi import FastAPI
from . models import Base

from .services import db_session, engine

db = db_session.session_factory()

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def home():
    return {"Message":"Hello cambodia"}
