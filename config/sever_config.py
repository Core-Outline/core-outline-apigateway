from dotenv import load_dotenv
from pathlib import Path
import os
from pymongo import MongoClient


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)

env_var = os.environ

servers = {
    "mongodb": 'mongodb',
    "mysql": 'MYSQL_SERVER',
    "csv": 'CSV_SERVER',
    "ml": 'ML_SERVER',
    "postgress": 'POSTGRESS_SERVER',
    "social_media": 'SOCIAL_MEDIA_SERVER'
}


port = 5000
