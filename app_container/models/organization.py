from app_container.services.organization_service import OrganizationService


class Organization:
    def __init__(self):
        self.organizationService = OrganizationService()

    def create(self, organization):
        return self.organizationService.create_organization(organization)

    def get(self, organization):
        return self.organizationService.get_organization(organization)

    def fetch(self, organization):
        return self.organizationService.fetch_organization(organization)

    def update(self, organization):
        return self.organizationService.update_organization(organization)
