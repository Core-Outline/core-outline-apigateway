from app.repositories.database import createClient, create, get, fetch, update
from config.organization_config import organization_table


class OrganizationService():
    def __init__(self):
        self.db = createClient()

    def create_user(self, organization):
        return create(self.db, organization_table, organization)

    def get_user(self, organization):
        return get(self.db, organization_table, organization)

    def fetch_user(self, organization):
        return fetch(self.db, organization_table, organization)

    def update_user(self, organization):
        return update(self.db, organization_table, organization)
