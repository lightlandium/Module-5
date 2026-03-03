from functools import reduce

# Пример списка чисел
numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

# 1. Используем map() для возведения в куб
def cube(x):
    """Возвращает куб числа x."""
    return x ** 3

cubes = list(map(cube, numbers))
print("Кубы чисел:", cubes)

# 2. Используем filter() для отбора чисел, кратных 5
def divisible_by_5(x):
    """Возвращает True, если x кратно 5."""
    return x % 5 == 0

multiples_of_5 = list(filter(divisible_by_5, numbers))
print("Числа, кратные 5:", multiples_of_5)

# 3. Используем filter() для отбора нечётных и reduce() для нахождения их произведения
def is_odd(x):
    """Возвращает True, если x нечётное."""
    return x % 2 != 0

def multiply(a, b):
    """Возвращает произведение a и b."""
    return a * b

odd_numbers = list(filter(is_odd, numbers))
product_of_odds = reduce(multiply, odd_numbers, 1)
print("Нечётные числа:", odd_numbers)
print("Произведение нечётных чисел:", product_of_odds)