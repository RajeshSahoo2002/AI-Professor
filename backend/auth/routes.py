from fastapi import FastAPI, APIRouter,HTTPException,Depends
from fastapi.security import HTTPBasic
from .model import *
from backend.config.db import users_collection
from .hash_utils import hash_password

router=APIRouter()
security=HTTPBasic()

# Endpoint is to signup the student
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
    # Below code is used to insert the user details in the database and the password will be stored in the hashed format and based on that it leaves a message and status code
    users_collection.insert_one({
        "fullname":req.fullname,
        "email":req.email,
        "username":req.username,
        "password":hashed_password,
        "grade":req.grade,
        "school":req.school
    })
    return {"message": "Student user created successfully"}

# Endpoint is to signup the teacher
@router.post("/signup/teacher")
def teacher_signup(req:teacherUser):
    """Handles the signup for a Teacher"""
    if users_collection.find_one({"username":req.username}):
        raise HTTPException(status_code=400, detail="Database already contains a user with the same username")
    
    if users_collection.find_one({"email":req.email}):
        raise HTTPException(status_code=500, detail="Email already registered")
    # Below code is to hash the password before getting it stored in the database so that if the user also logs in to check the db then he/she will not be able to see the password as well
    hashed_password=hash_password(req.password)
    
    # Below code is to insert the teachewr user details to the database and password will also be stored but in form of hashed one
    users_collection.insert_one({
        "fullname":req.fullname,
        "email":req.email,
        "username":req.username,
        "password":hashed_password,
        "subject":req.subject
    })
    return {"message":"Teacher user created successfully"}