from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_token

def get_api_token(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=402, detail='Invalid API key')
    
def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code = 401,  details='Invalid JWT Token')