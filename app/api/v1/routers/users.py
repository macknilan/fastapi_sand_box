"""Router Users"""

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

# ROUTES


@router.get("/", summary="First service for testing", status_code=status.HTTP_200_OK)
async def home():
    """
    Endpoint for test Hellow Word

    :return: {"Hello": "World"}
    """
    return {"Hello": "World"}
