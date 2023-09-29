from find_roots import find_roots
from decorator import find_roots_decorator

@find_roots_decorator
def find_and_save(a, b, c):
    return find_roots(a, b, c)

find_and_save("input.csv", "output.json")
