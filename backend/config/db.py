import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")
DB_NAME=os.getenv("DB_NAME")

client=MongoClient(MONGO_URI)
db=client[DB_NAME]

#Users collection is the collection which keeps the users records which we are making just like student and teachers records means their names, details that we are building the schema for that.
users_collection=db["users"]

