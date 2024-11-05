#represente mon objet application 
from fastapi import FastAPI, Form, Header, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic, OAuth2PasswordRequestForm
from user_model import UserModel
from loginCredentials import CredentialsLogin
from document_model import DocumentModel
from typing import Annotated
import jwt
import dotenv 
from os import environ 
from datetime import datetime, timedelta

app =FastAPI()

dotenv.load_dotenv()
SECRET_KEY = environ['SECRET_KEY']

@app.get('/')
def welcome_page(user_agent: Annotated[str, Header()]): 
    return {"message": "Welcome to FastAPI!", "headers": user_agent}

@app.get('/users/{username}')
def get_username(username: str): 
    return {'username': username}

@app.get('/documents/{document_id}')
def document_view(document_id: int, q: str | None = None): 
    return {"id": document_id, "name": "fake name", "querry": q }

@app.post('/users/new')
def add_new_user(user: UserModel): 
    """Create new User"""
    return {"user": user}

@app.post("/documents/")
def document_add(document: DocumentModel):
    """Create a new document."""
    return {"document": document}

@app.post("/login/")
async def login(credentials: Annotated[CredentialsLogin, Form()]):
    return {"username": credentials.username, "password": credentials.password}

@app.get('/login/basic')
def login_form_basic(creadentials: Annotated[HTTPBasicCredentials, Depends(HTTPBasic())]): 
    if not (creadentials.username == 'plop' and creadentials.password == 'plop'): 
        raise HTTPException(status_code=401, detail='invalid username or password')
    return {"username": creadentials.username, "password": creadentials.password}

@app.post('/login/token')
def login_token(credentials: Annotated[OAuth2PasswordRequestForm, Depends()]): 
    if not (credentials.username == 'plop' and credentials.password == 'plop'): 
        raise HTTPException(status_code=401, detail="invalid password or username")
    
    token = jwt.encode({"username": "plop", "email": "plop@gmail.com", "exp": datetime.now()+timedelta(hours=1) }, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
