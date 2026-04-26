# Here in main.py we will be creating the FastAPI instance and will be calling all the routes that are defined for all endpoints in routes.py
from fastapi import FastAPI
from backend.auth.routes import router as auth_router

app=FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def home():
    return {"message":"Welcome to the AI Professor API"}