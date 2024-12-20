from fastapi import APIRouter, HTTPException, Path
from bson import ObjectId
from app.database import db
from app.models import Post
from datetime import datetime

router = APIRouter()
error_response = "Post not found"

'''
We will be using the user_id from the URL and for the other contents we will be
refering to the body and then finally fill in the missing fields and update the table
'''
@router.post("/add/{user_id}/")
async def create_post(post: Post, user_id: str):
    post_dict = post.dict()
    post_dict["user_id"] = ObjectId(user_id)
    post_dict["created_at"] = datetime.now()
    post_dict["updated_at"] = datetime.now()

    print(user_id)

    result = db.posts.insert_one(post_dict)
    return {"message": "Post created successfully", "post_id": str(result.inserted_id)}

@router.get("/{post_id}/", response_model=Post)
async def get_post(post_id: str = Path(...)):
    try:
        newid = ObjectId(post_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Invalid ObjectId format having error {e}")
    
    post_obj = db.posts.find_one({"_id": newid})
    
    if post_obj:
        # Convert ObjectId to string for JSON serialization
        return post_obj
    else:
        raise HTTPException(status_code=404, detail="Post not found")
