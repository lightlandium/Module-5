# Задача 1: Сортировка учеников по возрасту
students_dict = {
    'Саша': 27,
    'Кирилл': 52,
    'Маша': 14,
    'Петя': 36,
    'Оля': 43,
}
sorted_students = sorted(students_dict.items(), key=lambda item: item[1])
for name, age in sorted_students:
    print(f"  {name}: {age}")

# Задача 2: Сортировка людей по индексу массы тела
data = [
    (82, 191),  # (вес в кг, рост в см)
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]
# Вычисляем ИМТ: вес / (рост_в_метрах ** 2), рост в метрах = рост_в_см / 100
sorted_by_bmi = sorted(data, key=lambda person: person[0] / ((person[1] / 100) ** 2))
for weight, height in sorted_by_bmi:
    bmi = weight / ((height / 100) ** 2)
    print(f"  Вес: {weight} кг, рост: {height} см, ИМТ: {bmi:.2f}")

# Задача 3: Самый младший ученик
students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]
youngest = min(students_list, key=lambda student: student['age'])
print(f"  {youngest['name']}, возраст {youngest['age']}")