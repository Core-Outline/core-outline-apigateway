import numpy as np
arr = [
    {
        "_id": "62dd2ee89ed4e5198766955d",
        "amount": 300,
        "user_id": "1234",
        "__v": 0
    },
    {
        "_id": "62dd30cfd411030174895903",
        "amount": 300,
        "user_id": "1234",
        "__v": 0
    }
]

final_obj = {}
columns = np.array([[key for key in obj.keys()] for obj in arr]).flatten()
columns = [val for val in columns]
print(columns)
