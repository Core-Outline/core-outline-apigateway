from app_container.repositories.database import createClient, create, fetch, get
from config.user_config import user_table
from app_container.repositories.encryption import pwdComparison, pwdEncryption
from app_container.repositories.jwt_ import encode


class AuthService():
    def __init__(self):
        self.db = createClient()

    def signin(self, auth):
        user = fetch(self.db, user_table, {"email": auth['email']})[0]
        pwdMatch = pwdComparison(
            password=auth['password'], hashedPassword=user['password'])
        if (pwdMatch == True):
            return encode(user)

    def signup(self, auth):
        auth['password'] = pwdEncryption(auth['password'])

        user = create(self.db, user_table, auth)
        user = get(self.db, user_table, {"_id": user['_id']})
        return encode(user)
