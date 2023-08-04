from dotenv import load_dotenv
from pathlib import Path
import os
from pymongo import MongoClient


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)

env_var = os.environ

servers = {
    "mongodb": env_var['ATLAS_MONGODB_SERVER'],
    "mysql": env_var['MYSQL_SERVER'],
    "csv": env_var['CSV_SERVER'],
    "ml": env_var['ML_SERVER'],
    "postgress": env_var['POSTGRESS_SERVER'],
    "social_media": env_var['SOCIAL_MEDIA_SERVER']
}


port = env_var['PORT']
