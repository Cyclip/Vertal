import pymongo
import os
import dotenv

dotenv.load()

MONGO_CLIENT = pymongo.MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
# Databases:
# "server": Server related stuff (users, etc.)
# "applications": List of application details
# "surveys": Survey details