obj = {
    "LastName": {
        "0": "Doe",
        "1": "Smith",
        "2": "Johnson"
    },
    "Salary": {
        "0": 5000.0,
        "1": 6000.0,
        "2": 5500.0
    }
}


final_result = {}
columns = [key for key in obj.keys()]
for col in columns:
    vals = [v for v in obj[col].values()]
    final_result[col] = vals

print(final_result)
