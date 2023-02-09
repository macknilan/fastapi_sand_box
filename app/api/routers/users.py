"""
Router Users
"""

# Pydantic
from pydantic import EmailStr

# fastpi
from fastapi import (
    APIRouter,
    status,
    Path,
    Query,
    Form,
    Header,
    Cookie,
    UploadFile,
    HTTPException,
)

# Models
# from api.models.user import Location, Person
# from ..models.user import Location, Person

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def root():
    return {"message": "Welcome to my bookstore app!"}













