import random

def guess_number():
    secret_number = random.randint(0, 1000)
    attempts = 10
    
    while attempts > 0:
        guess = int(input("Угадайте число (от 0 до 1000): "))
        
        if guess == secret_number:
            print("Поздравляю, вы угадали число!")
            return
        
        if guess < secret_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        
        attempts -= 1
        print(f"Осталось попыток: {attempts}")
    
    print(f"К сожалению, вы не угадали число. Загаданное число: {secret_number}")

guess_number()