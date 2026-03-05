import csv
import json

# Задание 0: Чтение данных из JSON
# Файл содержит словарь, где ключи — имена студентов, значения — их данные
with open('student_list.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

# Вспомогательная функция для вычисления среднего балла студента
def calculate_average(grades_dict):
    """Принимает словарь оценок, возвращает среднее арифметическое."""
    if not grades_dict:  # если оценок нет, возвращаем 0
        return 0
    return sum(grades_dict.values()) / len(grades_dict)


# Задание 1: Средний балл по всем предметам
def get_average_score():
    """
    Вычисляет средний балл по всем предметам для каждого студента
    и выводит результат в заданном формате.
    """
    for name, info in students.items():
        avg = calculate_average(info['grades'])
        print(f"Средний балл для студента {name}: {avg}")


get_average_score()
print()


# Задание 2: Наилучший и худший студент
def get_best_student():
    """Возвращает имя и средний балл студента с максимальным средним баллом."""
    if not students:
        return None, -1
    best_name = None
    best_avg = -1
    for name, info in students.items():
        avg = calculate_average(info['grades'])
        if avg > best_avg:
            best_avg = avg
            best_name = name
    return best_name, best_avg


def get_worst_student():
    """Возвращает имя и средний балл студента с минимальным средним баллом."""
    if not students:
        return None, float('inf')
    worst_name = None
    worst_avg = float('inf')
    for name, info in students.items():
        avg = calculate_average(info['grades'])
        if avg < worst_avg:
            worst_avg = avg
            worst_name = name
    return worst_name, worst_avg


best_name, best_avg = get_best_student()
worst_name, worst_avg = get_worst_student()


# Проверка на пустой список студентов перед выводом
if not students:
    print("Нет данных о студентах.")
else:
    print(f"Наилучший студент: {best_name} (Средний балл: {best_avg:.2f})")
    print(f"Худший студент: {worst_name} (Средний балл: {worst_avg:.2f})")
print()


# Задание 3: Поиск по имени
def find_student(name):
    """
    Ищет студента по имени и выводит его информацию.
    Если студент не найден, выводит соответствующее сообщение.
    """
    if name in students:
        info = students[name]
        print(f"Имя: {name}")                         # имя берём из ключа
        print(f"Возраст: {info['age']}")
        print(f"Предметы: {info['subjects']}")
        print(f"Оценки: {info['grades']}")
    else:
        print("Студент с таким именем не найден")


find_student("John")
print()
find_student("Emma")
print()


# Задание 4 сортировка студентов
def sort_students_by_average():
    """
    Возвращает список кортежей (имя, средний балл),
    отсортированный по убыванию среднего балла.
    """
    averages = []
    for name, info in students.items():
        avg = calculate_average(info['grades'])
        averages.append((name, avg))
    # Сортировка по убыванию среднего балла
    averages.sort(key=lambda x: x[1], reverse=True)
    return averages


sorted_students = sort_students_by_average()
print("Сортировка студентов по среднему баллу:")
if not sorted_students:
    print("Нет данных о студентах.")
else:
    for name, avg in sorted_students:
        print(f"{name}: {avg:.2f}")
print()


# Задание 5
students_list = []
for name, info in students.items():
    student_copy = info.copy()      # создаём копию, чтобы не менять исходные данные
    student_copy['name'] = name
    students_list.append(student_copy)


# Задание 6: Формирование CSV-файла
def generate_csv(filename='students_grades.csv'):
    """
    Создаёт CSV-файл с заголовками name, age, grade.
    grade — средний балл студента, округлённый до одного знака после запятой.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'age', 'grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Используем students_list, где уже есть поле 'name'
        for student in students_list:
            avg = calculate_average(student['grades'])
            writer.writerow({
                'name': student['name'],
                'age': student['age'],
                'grade': round(avg, 1)
            })


generate_csv()
print("CSV-файл 'students_grades.csv' успешно создан.")
