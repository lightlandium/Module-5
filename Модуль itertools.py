import itertools

# Задача 1: Комбинации чисел из списка

numbers = [1, 2, 3, 4]
combinations = list(itertools.combinations(numbers, 2))
for comb in combinations:
    print(comb)
print()

# Задача 2: Перестановки букв в слове "Python"

word = 'Python'
permutations = list(itertools.permutations(word))
for perm in permutations:
    print(''.join(perm))
print()

# Задача 3: Объединение списков в цикле 5 раз

list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']

combined = tuple(list1 + list2 + list3)

repeated = list(itertools.islice(itertools.cycle(combined), 5 * len(combined)))
print(repeated)
print()

# Задача 4: Генерация бесконечной последовательности Фибоначчи (первые 10 чисел)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)
print()

# Задача 5: Все возможные комбинации слов из двух списков

colors = ['red', 'blue']
items = ['shirt', 'shoes']
products = list(itertools.product(colors, items))
for prod in products:
    print(prod)