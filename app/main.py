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

from .api.v1.api_urls import router as urls

app = FastAPI(
    # root_path="/app/v1",
    # openapi_url="/app/v1/openapi.json",
    title="FastAPI Aws Lambda",
    version="0.0.1",
    description="☠",
    # contact={"name": "mack", "url": "http://mack.host"},
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
)


app.include_router(urls)
# app.include_router(sign_in.router)
# app.include_router(movies.router)
# app.include_router(authorization.router)

# aws lambda
handler = Mangum(app)
