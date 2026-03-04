# Задание 1: фильтр строк длиной больше 4
strings = ["apple", "kiwi", "banana", "fig"]
long_strings = list(filter(lambda s: len(s) > 4, strings))
print("Длина > 4:", long_strings)

# Задание 2: студент с максимальной оценкой
students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]
best_student = max(students, key=lambda s: s["grade"])
print("Макс. оценка:", best_student)

# Задание 3: сортировка кортежей по сумме элементов
tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_tuples = sorted(tuples, key=lambda t: t[0] + t[1])
print("По сумме:", sorted_tuples)

# Задание 4: фильтр чётных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Чётные числа:", evens)

# Задание 5: сортировка объектов класса Person по возрасту
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

people = [Person("Alice", 28), Person("Gwen", 25), Person("Marie", 32)]
sorted_people = sorted(people, key=lambda p: p.age)
print("Сортировка по возрасту:", sorted_people)