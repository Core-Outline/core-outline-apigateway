from dotenv import load_dotenv
from pathlib import Path
import os
from pymongo import MongoClient


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)

env_var = os.environ


db_username = 'tomitsuma'
db_password = 'Tobirama13'
db_database = 'CoreOutline'
