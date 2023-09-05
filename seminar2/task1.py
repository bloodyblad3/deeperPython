def decimaltohex(number):
    hex_digits = "0123456789ABCDEF"
    if number == 0:
        return "0"
    
    hex_string = ""
    while number > 0:
        rem = number % 16
        hex_string = hex_digits[rem] + hex_string
        number = number // 16
    
    return hex_string
    
    return hexstring

num = int(input("Введите целое число: "))
hexnum = decimaltohex(num)
print("Шестнадцатеричное представление числа:", hexnum)