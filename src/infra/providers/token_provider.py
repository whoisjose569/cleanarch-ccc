from jose import jwt
from datetime import datetime, timedelta
from os import getenv

def create_access_token (data: dict):
    dataa = data.copy()
    expirate = datetime.utcnow() + timedelta(minutes=3000)
    
    dataa.update({'exp': expirate})
    
    token_jwt = jwt.encode(dataa, 'd5f89ffc524b1724572e80ed5b207b482bfa8a92', algorithm='HS256')
    return token_jwt

def verify_access_token(token: str):
    charge = jwt.decode(token, 'd5f89ffc524b1724572e80ed5b207b482bfa8a92', algorithms=['HS256'])
    return charge.get('sub')
