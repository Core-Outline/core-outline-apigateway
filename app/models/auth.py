from app.auth_service import AuthService


class Auth:
    def __init__(self):
        self.authService = AuthService()

    def signin(self, auth):
        return self.authService.signin(auth)

    def signup(self, auth):
        return self.authService.signup(auth)
