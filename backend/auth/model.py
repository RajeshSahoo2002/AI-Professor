#this file contains the creation of the datamodel for for the user schema i.e. for the students and professors
from pydantic import BaseModel

# Mongo DB generates a by-default ID so we don't need to include a id while we are define the models 
class studentUser(BaseModel):
    #id: int
    fullname: str
    email: str
    username: str
    password: str
    grade: int
    school: str
    
class teacherUser(BaseModel):
    # id: int
    fullname: str
    email: str
    username: str
    password: str
    subject: str