from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime
from typing import Optional, List

#Defined and configured pydantic for type safety and better outputs

class User(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    username: str
    email: str
    hashed_password: str
    linked_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat() if v else None
        }

class LinkIdRequest(BaseModel):
    user_id: str = Field(..., description="User id as astring")
    linked_id: str = Field(..., description="Linked id as a string")


class LinkedData(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    user_id: ObjectId
    linked_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat() if v else None
        }

class Post(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    user_id: Optional[ObjectId] = None
    title: str
    content: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
            ObjectId: str
        }

class JoinedData(BaseModel):
    _id: ObjectId
    username: str
    email: str
    user_posts: List[Post]
    linked_data: List[LinkedData]
