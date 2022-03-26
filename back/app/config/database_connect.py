import os

from pymongo import MongoClient

mongo_url = (
    "mongodb://"
    + os.environ["MONGO_INITDB_ROOT_USERNAME"]
    + ":"
    + os.environ["MONGO_INITDB_ROOT_PASSWORD"]
    + "@"
    + os.environ["MONGODB_HOSTNAME"]
    + ":27017/"
)

try:
    connection = MongoClient(mongo_url)
    db = connection["upmarket"]
    print(connection.server_info())
except:
    print("connection failed")
