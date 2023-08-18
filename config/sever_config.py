from dotenv import load_dotenv
from pathlib import Path
import os
from pymongo import MongoClient


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)

env_var = os.environ

servers = {
    "mongodb": 'http://127.0.0.1:4000',
    "mysql": 'http://127.0.0.1:6000',
    # "csv": 'CSV_SERVER',
    "ml": 'http://127.0.0.1:3000',
    # "postgress": 'POSTGRESS_SERVER',
    # "social_media": 'SOCIAL_MEDIA_SERVER'
}


port = 5000
