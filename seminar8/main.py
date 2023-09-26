import os
import json
import csv
import pickle

def get_directory_info(directory):
    def get_size(path):
        if os.path.isfile(path):
            return os.path.getsize(path)
        elif os.path.isdir(path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            return total_size
        else:
            return None

    def collect_info(path):
        if os.path.isfile(path):
            return {
                "name": os.path.basename(path),
                "type": "file",
                "size": get_size(path)
            }
        elif os.path.isdir(path):
            return {
                "name": os.path.basename(path),
                "type": "directory",
                "size": get_size(path)
            }

    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            info = collect_info(file_path)
            results.append(info)

    return results

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, output_file):
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

directory = 'C:/Users/keruvim/deeperPython'
data = get_directory_info(directory)

save_to_json(data, 'directory_info.json')
save_to_csv(data, 'directory_info.csv')
save_to_pickle(data, 'directory_info.pkl')
