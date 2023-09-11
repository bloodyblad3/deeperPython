import os

def split_path(filepath):
    path, filename = os.path.split(filepath)
    name, extension = os.path.splitext(filename)
    return path, name, extension

filepath = 'deeperPython/seminar5/task2.py'
path, name, extension = split_path(filepath)
print(f"Путь - {path} \nИмя файла - {name} \nРасширение - {extension}")