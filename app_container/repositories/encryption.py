import bcrypt
from config.encryption_config import salt


def pwdEncryption(password):
    return bcrypt.hashpw(password, salt)


def pwdComparison(password, hashedPassword):
    return bcrypt.checkpw(password, hashedPassword)
