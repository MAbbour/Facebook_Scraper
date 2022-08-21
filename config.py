from pymongo import MongoClient
client = MongoClient()

db = client["TestDB"]
msg_collection = db["messages"]