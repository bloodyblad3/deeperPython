balance = 5000000
operations_history = []

def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    fee = max(fee, 30)
    fee = min(fee, 600)
    return fee

def calculate_tax(amount):
    return amount * 0.1

def update_balance(amount):
    global balance
    
    if balance > 5000000:
        tax = calculate_tax(amount)
        balance -= tax
    
    balance += amount

def deposit(amount):
    update_balance(amount)
    operations_history.append(("Пополнение", amount))

def withdraw(amount):
    global balance
    
    if amount % 50 == 0:
        if amount <= balance:
            fee = calculate_withdrawal_fee(amount)
            update_balance(-amount - fee)
            operations_history.append(("Снятие", amount, fee))
        else:
            print("Недостаточно средств на счете!")
    else:
        print("Сумма снятия должна быть кратна 50 у.е.")

def display_balance():
    print("Баланс:", balance, "у.е.")

def display_operations_history():
    print("История операций:")
    for operation in operations_history:
        if len(operation) == 2:
            operation_type, amount = operation
            print(operation_type + ":", amount, "у.е.")
        else:
            operation_type, amount, fee = operation
            print(operation_type + ":", amount, "у.е., комиссия:", fee, "у.е.")

def atm_program():
    while True:
        action = int(input("Выберите действие: \n1 - пополнить \n2 - снять \n3 - баланс \n4 - история \n5 - выйти\n"))
        
        if action == 1:
            amount = int(input("Введите сумму для пополнения: "))
            
            if amount % 50 == 0:
                deposit(amount)
                print("Баланс:", balance, "у.е.")
            else:
                print("Сумма пополнения должна быть кратна 50 у.е.")
        
        elif action == 2:
            amount = int(input("Введите сумму для снятия: "))
            withdraw(amount)
            print("Баланс:", balance, "у.е.")
        
        elif action == 3:
            display_balance()
        
        elif action == 4:
            display_operations_history()
        
        elif action == 5:
            break
        
        else:
            print("Некорректное действие! Пожалуйста, повторите ввод.")

atm_program()
