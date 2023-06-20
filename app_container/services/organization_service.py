from app_container.repositories.database import createClient, create, get, fetch, update
from config.organization_config import organization_table


class OrganizationService():
    def __init__(self):
        self.db = createClient()

    def create_organization(self, organization):
        return create(self.db, organization_table, organization)

    def get_organization(self, organization):
        return get(self.db, organization_table, organization)

    def fetch_organization(self, organization):
        return fetch(self.db, organization_table, organization)

    def update_organization(self, organization):
        return update(self.db, organization_table, organization)
