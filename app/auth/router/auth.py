from fastapi import APIRouter, Depends,HTTPException, Request, status
from sqlalchemy.orm import Session

from ..crud import user
from .. import schema
from ... import models
from ...utils import database

router = APIRouter()

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)




