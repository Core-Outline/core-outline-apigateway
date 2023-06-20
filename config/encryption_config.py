from dotenv import load_dotenv
from pathlib import Path
import os
import bcrypt


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)


env_var = os.environ

salt = bcrypt.gensalt()
