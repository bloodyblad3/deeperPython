def create_dict(**kwargs):
    result = {}
    
    for key, value in kwargs.items():
        if hash(key):
            result[value] = key
        else:
            result[str(value)] = key
    
    return result

dictionary = create_dict(a=10, b=20, c=30, d=4, e=5, f=100)
print(dictionary)