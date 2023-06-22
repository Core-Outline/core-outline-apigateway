import numpy as np


def transform_mongodb(documents):
    final_obj = {}
    columns = np.array([[key for key in obj.keys()]
                       for obj in documents]).flatten()
    columns = set([val for val in columns])
    columns = [col for col in columns]

    for col in columns:
        final_obj[col] = [val for val in [obj[col] for obj in documents]]
    return (final_obj)
