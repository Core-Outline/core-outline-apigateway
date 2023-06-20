from app_container.repositories.database import createClient, create, get, fetch, update
from config.user_config import user_table


class UserService():
    def __init__(self):
        self.db = createClient()

    def create_user(self, user):
        return create(self.db, user_table, user)

    def get_user(self, user):
        return get(self.db, user_table, user)

    def fetch_user(self, user):
        return fetch(self.db, user_table, user)

    def update_user(self, user):
        return update(self.db, user_table, user)
