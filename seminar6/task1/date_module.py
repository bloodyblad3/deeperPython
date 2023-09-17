# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, 
# если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        
        if year < 1 or year > 9999:
            return False
        
        if month < 1 or month > 12:
            return False
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if is_leap_year(year):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        else:
            return False
        
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    date_str = input("Введите дату в формате DD.MM.YYYY: ")
    if is_valid_date(date_str):
        print("Дата является валидной.")
    else:
        print("Дата не является валидной.")