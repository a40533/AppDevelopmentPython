from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    username: str
    short_bio: str

def get_user_info() -> (str, str):
    username = "test user"
    short_bio = "test bio"
    return username, short_bio

@app.get("/user/me", response_class=User)
def home():
    
    username, short_bio = get_user_info()
    
    user= User(username=username, short_bio=short_bio)
    return User

print("hello world")