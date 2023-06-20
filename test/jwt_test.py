import jwt

token = jwt.encode({"pay": "payload"}, key="124567", algorithm='HS256')
print(token)
