import requests
import json

obj = json.dumps({
    "data_source_name": "MyTrial",
    "username": "thomasTsuma",
    "password": "GR^KX$uRe9#JwLc6",
    "user_id": "1234567",
    "type": "mysql",
    "server": "192.168.5.18\\CROPNUT",
}, sort_keys=True)
response = requests.post(
    url='http://127.0.0.1:6000/data-source/create-data-source',
    data=obj,
    headers={
        "Content-Type": "application/json"
    },
)

print(response.json())
