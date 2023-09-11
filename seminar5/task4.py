def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
n = int(input("Введите желаемое кол-во чисел фибоначчи: "))
for i in range(n):
    print(next(fib_gen))