import date_module

if __name__ == "__main__":
    date_str = input("Введите дату в формате DD.MM.YYYY: ")
    if date_module.is_valid_date(date_str):
        print("Дата является валидной.")
    else:
        print("Дата не является валидной.")