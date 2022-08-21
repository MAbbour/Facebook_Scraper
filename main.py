import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from scraper import Scraper
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

DB = "TestDB"
MSG_COLLECTION = "messages"


class Message(BaseModel):
    text: str
    time: str
    reactions: str


app = FastAPI()
list = Scraper()


@app.get("/status")
async def get_status():
    """Get status of messaging server."""
    return {"status": "running"}

@app.post("/post_message", status_code=status.HTTP_201_CREATED)
def post_message(message: Message):
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        data = list.scrapedata()
        for i in range(len(data)):
            result = msg_collection.insert_one(data[i])
            ack = result.acknowledged
            return {"insertion": ack}



@app.get("/list")
async def display_collection(request: Request):
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.find()
        return distinct_channel_list


if __name__ == "__main__":
    uvicorn.run(app='main:app')