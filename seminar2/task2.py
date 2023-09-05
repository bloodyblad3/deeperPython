# нахождение НОД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# сокращение дроби
def simplify_fraction(num, denom):
    common_divisor = gcd(num, denom)
    return num // common_divisor, denom // common_divisor

# сложение дробей
def add_fractions(num1, denom1, num2, denom2):
    common_denominator = denom1 * denom2
    new_num1 = num1 * denom2
    new_num2 = num2 * denom1
    result_num = new_num1 + new_num2
    return simplify_fraction(result_num, common_denominator)

# умножение дробей
def multiply_fractions(num1, denom1, num2, denom2):
    result_num = num1 * num2
    result_denom = denom1 * denom2
    return simplify_fraction(result_num, result_denom)

def main():
    input_str1 = input("Введите первую дробь (в формате a/b): ")
    input_str2 = input("Введите вторую дробь (в формате a/b): ")

    num1, denom1 = map(int, input_str1.split('/'))
    num2, denom2 = map(int, input_str2.split('/'))

    sum_result = add_fractions(num1, denom1, num2, denom2)
    product_result = multiply_fractions(num1, denom1, num2, denom2)

    print(f"Сумма: {sum_result[0]}/{sum_result[1]}")
    print(f"Произведение: {product_result[0]}/{product_result[1]}")

if __name__ == "__main__":
    main()