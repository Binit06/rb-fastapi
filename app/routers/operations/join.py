from fastapi import APIRouter, HTTPException, Path
from app.database import db
from bson import ObjectId
from app.models import JoinedData
from typing import List

router = APIRouter()

'''
We will be using the user_id and then conver it to an instance of ObjectId for usecases
We will then compare all the results where _id will be the same as user_id and then
match the same for post data and even for linked_data. After the multi query is 
completed we can return the results.
'''
@router.get("/joined-data/{user_id}/", response_model=JoinedData)
async def get_joined_data(user_id: str = Path(...)):
    try:
        # Convert user_id to ObjectId
        obj_id = ObjectId(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid user_id error: {e}")

    pipeline = [
        {"$match": {"_id": obj_id}},
        {"$lookup": {
            "from": "posts",
            "localField": "_id",
            "foreignField": "user_id",
            "as": "user_posts"
        }},
        {"$lookup": {
            "from": "linked_data",
            "localField": "_id",
            "foreignField": "user_id",
            "as": "linked_data"
        }},
        {"$addFields": {
            "user_posts": {"$ifNull": ["$user_posts", []]},
            "linked_data": {"$ifNull": ["$linked_data", []]}
        }}
    ]

    joined_data = list(db.users.aggregate(pipeline))
    if joined_data:
        return joined_data[0]  # Assuming unique user_id, return the first document
    else:
        raise HTTPException(status_code=404, detail="Joined data not found")

