import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    PROJECT_NAME = 'Car Price'
    API_KEY = os.getenv('API_KEY', 'demo_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','secret')
    JWT_ALGORITHM = 'HS256'
    REDIS_URL = os.getenv('REDIS_URL')
    MODEL_PATH = 'app/model/model.pkl'

settings = Settings()