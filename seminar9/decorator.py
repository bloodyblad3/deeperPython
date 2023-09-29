import csv
import json
import functools

def find_roots_decorator(func):
    def wrapper(input_csv, output_json):
        results = []
        with open(input_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                results.append({
                    "coefficients": (a, b, c),
                    "roots": roots
                })
        
        with open(output_json, 'w') as json_file:
            json.dump(results, json_file, indent=4)
    
    return wrapper
