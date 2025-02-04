from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def authenticate_user(request: Request):
    token = await oauth2_scheme(request)
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    # Add your token validation logic here
    # For example, decode the token and check its validity
