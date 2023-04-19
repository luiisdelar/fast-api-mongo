from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jose import jws

security = HTTPBearer()

# Middleware para decodificar token
def decode_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        decoded_token = jws.verify(token, 'uzAqLLeWwiZcvzM0h22sGt5onB1b53ea', algorithms=["HS256"])
        return decoded_token
    except:
        raise HTTPException(status_code=401, detail="Token invalido")
    
