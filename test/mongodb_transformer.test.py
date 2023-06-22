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
columns = set([val for val in columns])
columns = [col for col in columns]
print(columns)

for col in columns:
    final_obj[col] = [val for val in [obj[col] for obj in arr]]

print(final_obj)
