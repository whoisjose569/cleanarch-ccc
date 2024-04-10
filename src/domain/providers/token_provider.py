from jose import jwt
from datetime import datetime, timedelta
from os import getenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jose import jwt, JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token (data: dict):
    dataa = data.copy()
    expirate = datetime.utcnow() + timedelta(minutes=30)
    
    dataa.update({'exp': expirate})
    
    token_jwt = jwt.encode(dataa, 'd5f89ffc524b1724572e80ed5b207b482bfa8a92', algorithm='HS256')
    return token_jwt

async def verify_access_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, 'd5f89ffc524b1724572e80ed5b207b482bfa8a92', algorithms=['HS256'])
        return payload
    except JWTError:
        raise(HTTPException(status_code=401, detail="Invalid or expired token"))
