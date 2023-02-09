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
from fastapi import FastAPI

# Mangum aws lambda
from mangum import Mangum

from .api.routers.users import router_user

app = FastAPI()
app.include_router(router_user)


# aws lambda
handler_user = Mangum(router_user, lifespan="off")



