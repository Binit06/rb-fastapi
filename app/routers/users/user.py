from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import User, LinkIdRequest
import bcrypt
from datetime import datetime
from typing import List

router = APIRouter()

@router.post("/register/")
async def register_user(user: User):
    user_dict = user.dict()
    # Step 1 : We will be hashing the password and updating the dictionary
    hashed_password = bcrypt.hashpw(user_dict['hashed_password'].encode('utf-8'), bcrypt.gensalt())
    user_dict['hashed_password'] = hashed_password.decode('utf-8')  # Store hashed password as string

    # Step 2 : We will fill the missing fields
    user_dict['created_at'] = datetime.now()
    user_dict['updated_at'] = datetime.now()

    # Step 3 : We will be inserting the data into the users
    result = db.users.insert_one(user_dict)
    return {"message": "User Registered Successfully", "user_id": str(result.inserted_id)}

@router.post("/link-id/")
async def link_id(link_id_request: LinkIdRequest):
    user_id = link_id_request.user_id
    linked_id = link_id_request.linked_id
    # Step 1 : We will update the users with the linked_id
    result = db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"linked_id": linked_id}})
    if result.modified_count != 1:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    # Step 2 : We will update the linked_data with the linked_id or just add a new data
    result_linked_data = db.linked_data.update_many({"user_id": ObjectId(user_id)}, {"$set": {"linked_id": linked_id, "updated_at": datetime.now()}}, upsert=True)
    print(result_linked_data)
    return {"message": "ID Linked Successfully"}

# The below functions are just some basic CRUD operations to fetch the data in different ways.

@router.get('/user/{user_id}/', response_model=User)
async def get_user(user_id: str):
    user_data = db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return user_data
    else:
        raise HTTPException(status_code=404, detail="User Not Found")

@router.get("/user_email/", response_model=User)
async def get_user_by_email(email: str):
    user_data = db.users.find_one({"email": email})
    if user_data:
        return user_data
    else:
        raise HTTPException(status_code=404, detail="User with this email not found")

@router.get('/all_users/', response_model=List[User])
async def get_all_users():
    users_data = list(db.users.find())
    return users_data

@router.get('/hello/')
async def hello_world():
    return {"message": "Hello, World!"}
