"""
Script de FastAPI de hello word
In Python 3.10.6
Run:
    uvicorn main:app --reload
"""
# import os
# import sys
#
# sys.path.append(os.path.join(os.path.dirname(__file__)))

# fastpi
from fastapi import FastAPI, APIRouter

# Mangum aws lambda
from mangum import Mangum

from .api.routers import users

app = FastAPI()

router_user = APIRouter()

app.include_router(users.router)


# aws lambda
# handler = Mangum(app)

handler_user = Mangum(router_user)
