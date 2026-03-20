from fastapi import FastAPI, APIRouter,HTTPException,Depends
from fastapi.security import HTTPBasic
from .model import *
from config.db import users_collection
from .hash_utils import hash_password

router=APIRouter()
security=HTTPBasic()

@router.post("/signup/student")
def student_signup(req:studentUser):
    """Handles the student signup request"""
    #Below if condition is to check if the username already exists or not and based on that it leaves a message and status code
    if users_collection.find_one({"username":req.username}):
        raise HTTPException(status_code=400, detail="User already exists in the database")
    
    if users_collection.find_one({"email":req.email}):
        raise HTTPException(status_code=500, detail="Email already registered")
    
    #hash the passwords before getting the password stored in database
    hashed_password=hash_password(req.password)
    users_collection.insert_one({
        "id":req.id,
        "fullname":req.fullname,
        "email":req.email,
        "username":req.username,
        "password":hashed_password,
        "grade":req.grade,
        "school":req.school
    })
    return {"message": "Student user created successfully"}