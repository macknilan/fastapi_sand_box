from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def root():
    """
    Docs
    """
    return {"message": "Up and running!"}


handler = Mangum(app)
