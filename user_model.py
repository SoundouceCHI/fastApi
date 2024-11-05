from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel): 
    """validate user"""
    username: str
    age: int = Field(default=18, gt=0, lt=120)
    email: EmailStr