import bcrypt
from config.encryption_config import salt


def pwdEncryption(password):
    return str(bcrypt.hashpw(str(password).encode('utf-8'), salt).decode('utf-8'))


def pwdComparison(password, hashedPassword):
    return bcrypt.checkpw(password.encode('utf-8'), hashedPassword.encode('utf-8'))
