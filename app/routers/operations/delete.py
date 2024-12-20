from fastapi import APIRouter, HTTPException
from app.database import db
from bson import ObjectId

router = APIRouter()

'''
We will move one by one from user then to linked data and then to post for removing all the data having user_id 
same as that of the provided user_id
'''
@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    # Delete user from 'users' collection
    result_users = db.users.delete_one({"_id": ObjectId(user_id)})
    if result_users.deleted_count != 1:
        raise HTTPException(status_code=404, detail="User not found")

    # Delete associated data from other collections (example: 'posts' and 'comments')
    result_linked = db.linked_data.delete_many({"user_id": ObjectId(user_id)})
    result_posts = db.posts.delete_many({"user_id": ObjectId(user_id)})

    return {"message": f"User and associated data deleted successfully. Deleted {result_linked.deleted_count} linked ids and {result_posts.deleted_count} posts."}
