import bcrypt
from config.encrytion_configs import salt


def pwdEncryption(password):
    return bcrypt.hashpw(password, salt)


def pwdComparison(password, hashedPassword):
    return bcrypt.checkpw(password, hashedPassword)
