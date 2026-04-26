# ...existing code...
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi
import re
# ...existing code...

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")
DB_NAME=os.getenv("DB_NAME")

client=MongoClient(MONGO_URI)
# sanitize DB name and ensure no invalid chars (optional but helpful)
DB_NAME = re.sub(r"[^A-Za-z0-9_.-]", "_", DB_NAME or "ai_professor")

# use certifi CA bundle so TLS certificate verification succeeds on macOS
client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000,  # 30s
    connectTimeoutMS=20000
)

db=client[DB_NAME]
# ...existing code...
users_collection=db["users"]