from app.repositories.database import createClient, create, get
from config.user_config import user_table
from app.repositories.encryption import pwdComparison, pwdEncryption


class AuthService():
    def __init__(self):
        self.db = createClient()

    def signin(self, auth):
        user = get(self.db, user_table, auth)
        pwdMatch = pwdComparison(
            password=auth.password, hashedPassword=user.password)
        if (pwdMatch == True):
            return user

    def signup(self, auth):
        auth['password'] = pwdEncryption(auth['password'])
        return create(auth)
