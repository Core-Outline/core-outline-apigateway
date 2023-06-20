import jwt
from config.app_configs import jwt_secret_key


def encode(payload, key=jwt_secret_key):
    return {"token": jwt.encode(payload=payload, key=jwt_secret_key)}
