def check_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a != b and b != c and a != c:
            return "Треугольник - разносторонний"
        elif a == b and b == c:
            return "Треугольник - равносторонний"
        else:
            return "Треугольник - равнобедренный"
    else:
        return "Треугольник не существует"

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

result = check_triangle(a, b, c)
print(result)