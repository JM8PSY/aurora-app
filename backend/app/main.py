from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Aurora Observation API")
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Aurora Observation API"}

