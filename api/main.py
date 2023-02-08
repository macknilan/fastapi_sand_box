"""
Script de FastAPI de hello word
In Python 3.10.6
Run:
    uvicorn main:app --reload
"""
import os
# import sys
#
# sys.path.append(os.path.join(os.path.dirname(__file__)))

# fastpi
from fastapi import FastAPI

# Mangum aws lambda
from mangum import Mangum

from .routers import users

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"


app = FastAPI(
    # root_path="/api/v1",
    # openapi_url="/api/v1/openapi.json",
    title="FastAPI Aws Lambda",
    version="0.0.1",
    description="☠",
    openapi_prefix=openapi_prefix
    # contact={"name": "mack", "url": "http://mack.host"},
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
)


app.include_router(users.router, prefix="/users")
# app.include_router(sign_in.router)
# app.include_router(movies.router)
# app.include_router(authorization.router)

# aws lambda
handler = Mangum(app=app)
