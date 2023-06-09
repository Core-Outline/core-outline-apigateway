from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)

env_var = os.getenv('.env')

salt = env_var['SALT']
