import json
import csv

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, name, user_id, access_level):
        if access_level not in range(1, 8):
            raise ValueError("Уровень доступа должен находиться в диапазоне от 1 до 7")
        
        for level in self.users.values():
            if user_id in level:
                raise ValueError("ID пользователя должен быть уникален.")
        
        if access_level not in self.users:
            self.users[access_level] = {}
        self.users[access_level][user_id] = name

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.users, file, indent=4)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'User ID', 'Access Level'])
            for level, user_dict in self.users.items():
                for user_id, name in user_dict.items():
                    writer.writerow([name, user_id, level])

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def print_users(self):
        for level, user_dict in self.users.items():
            for user_id, name in user_dict.items():
                print(f"ID: {user_id}, Имя: {name}, Уровень доступа: {level}")

def main():
    database = UserDatabase()
    database.load_from_json('user_data.json')

    while True:
        name = input("Введите имя пользователя (или 'q' для выхода): ")
        if name == 'q':
            break
        user_id = input("Введите ID пользователя: ")
        access_level = int(input("Введите уровень доступа (от 1 до 7): "))

        try:
            database.add_user(name, user_id, access_level)
            database.save_to_json('user_data.json')
            database.print_users()
        except ValueError as e:
            print(f"Ошибка: {e}")

    database.save_to_csv('user_data.csv')

if __name__ == "__main__":
    main()
