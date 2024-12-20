from fastapi import APIRouter, HTTPException
from app.database import db
import bcrypt

router = APIRouter()
'''
We will easily be just using the function verify password to hash the given password and match it with the previously hashed password
If they are the same we return true and hence validate the user
'''
def verify_password(plain_password: str, hash_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hash_password.encode("utf-8"))

@router.post("/login/")
async def login_user(email: str, password: str):
    user_data = db.users.find_one({"email": email})
    if user_data and verify_password(password, user_data['hashed_password']):
        return {"message": "Login Succesful", "user_id": str(user_data['_id'])}
    else:
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    
@router.get("/newpost/")
async def create_post():
    return {"message": "Login Succesful", "user_id": "Fuck you"}
