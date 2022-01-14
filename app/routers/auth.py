from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import models, schema, utils, oauth2
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['login']
)

@router.post('/login',response_model=schema.Token)
def login(user_credentials : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db) ):
    # OAuth2password form return {username : "",password : ""} dict
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    token = oauth2.create_access_token({"user_id" : user.id})
    return {"jwt_token" : token, "token_type": "Bearer"}