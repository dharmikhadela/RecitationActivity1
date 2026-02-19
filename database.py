import os
from pymongo import MongoClient

mongo_db = os.environ.get('MONGO_DB', "false")

if mongo_db == "true":
    print("Using Docker Compose DB")
    mongo_client = MongoClient("mongodb://mongo:27017")
else:
    print("Using local DB")
    mongo_client = MongoClient("mongodb://localhost:27017")

