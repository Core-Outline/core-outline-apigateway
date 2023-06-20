import bcrypt
salt = (bcrypt.gensalt())
# print(str(bcrypt.hashpw(str("password").encode('utf-8'), salt)))

password = 'password123'  # The password you want to check
# The hashed password to compare against
hashed_password = '$2b$12$6jB44RZT3.IkVcUbzi1yD.2T6hS6A8Rq6nbcTwg9F23t6HwzJ3yKG'

# Check if the entered password matches the hashed password
if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
    print("Password matches!")
else:
    print("Password does not match!")
