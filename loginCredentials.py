from pydantic import BaseModel, Field

class CredentialsLogin(BaseModel): 
    username: str
    password: str 