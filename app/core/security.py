from datetime import datetime, timedelta, timezone
from app.core.config import settings
from jose import JWTError,jwt

def create_token(data: dict, expire_minutes=30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({
        'exp': expire
    })

    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM
    )

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        return None