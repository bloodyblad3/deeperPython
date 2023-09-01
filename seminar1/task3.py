def is_prime(num):
    if num <= 1 or num > 100000:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Введите число: "))
if is_prime(num):
    print("Число является простым")
else:
    print("Число является составным")