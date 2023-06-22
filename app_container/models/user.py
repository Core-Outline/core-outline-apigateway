from app_container.services.user_service import UserService


class User:
    def __init__(self):
        self.userService = UserService()

    def create(self, user):
        return self.userService.create_user(user)

    def get(self, user):
        return self.userService.get_user(user)

    def fetch(self, user):
        return self.userService.fetch_user(user)

    def update(self, user):
        return self.userService.update_user(user)
