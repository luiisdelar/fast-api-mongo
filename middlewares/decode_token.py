from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jose import jws

security = HTTPBearer()

# Middleware para decodificar token
def decode_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    #try:
    
    token = credentials.credentials
    print(token)
    decoded_token = jws.verify(token, 'uzAqLLeWwiZcvzM0h22sGt5onB1b53ea', algorithms=["HS256"])
    print(decode_token)
    return decoded_token
    #except:
    #    raise HTTPException(status_code=401, detail="Token invalido")
    #C:\Users\Luis\Desktop\fastapi-mongo\entorno_virtual\lib\site-packages\jwt\__init__.py
    #/usr/local/lib/                               python3.11/site-packages/jwt/__init__.py