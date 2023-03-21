"""
Router for Authorization
"""

# Python

# Pydantic

# fastpi

from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from starlette.responses import JSONResponse

# Model

from api.models.user import SecretWord


# token

from api.jwt_manager import token_manager

router = APIRouter(prefix="/authorization", tags=["Authorization"])


@router.post(
    "/sing-in",
    # response_model=SecretWord,
    # response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="Sing In",
)
async def sing_in(user: SecretWord) -> JSONResponse:
    """
    Servicio que simula el SignIn de usuario y que cumpla el email y password
    en el if

    `:param email:`

    `:param: password:`

    `:return: token`
    """
    # user.password.get_secret_value()
    # if user.email == "admin@email.com" and user.password.get_secret_value() == "contrasena":
    if user.email == "johndoe@mail.com" and user.password == "password":
        token: str = token_manager.create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Credenciales no validas t(-_-t)"},
        )
