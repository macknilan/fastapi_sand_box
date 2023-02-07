"""
Manejador de elementos de seguridad.
"""

# Fastapi
from fastapi.security import HTTPBearer
from fastapi import status, HTTPException, Request

# token
# from api.jwt_manager import token_manager
from ..jwt_manager.token_manager import validate_token


class JWTBearer(HTTPBearer):
    """
    Middlewares de autenticación
    """
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "admin@email.com":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credenciales invalidas t(-_-t)")

