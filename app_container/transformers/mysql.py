def transform_mysql(obj):
    final_result = {}
    columns = [key for key in obj.keys()]
    for col in columns:
        vals = [v for v in obj[col].values()]
        final_result[col] = vals
    return final_result
