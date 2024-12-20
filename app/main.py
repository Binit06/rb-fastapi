from fastapi import FastAPI

from app.routers.post import post
from app.routers.auth import auth
from app.routers.operations import delete, join
from app.routers.users import user

app = FastAPI()

#Defining all the routes that are going to be called and applying a prefix for the routes
app.include_router(user.router, prefix="/user", tags=['user'])
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(join.router, prefix="/join", tags=['join'])
app.include_router(delete.router, prefix="/delete", tags=['delete'])
app.include_router(post.router, prefix="/post", tags=['post'])
