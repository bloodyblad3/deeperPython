import csv
import random

def check_filename(filename):
    ext = ".csv"
    if ext in filename:
        return filename
    else:
        return f"{filename + ext}" 

def generate_csv_file(filename, rows=100):
    if rows > 1000:
        print("Нельзя больше 1000!")
    else:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for _ in range(rows):
                row = [random.randint(1, 1000) for _ in range(3)]
                writer.writerow(row)

generate_csv_file(check_filename("input"), 500)