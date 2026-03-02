# Задание 1: Работа с файлом students.json
import json

# Чтение данных из файла
with open('students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

total_students = len(students)
print(f"Общее количество студентов: {total_students}")

# Поиск студента с самым высоким возрастом
max_age = -1
oldest_student = None
for s in students:
    if s['возраст'] > max_age:
        max_age = s['возраст']
        oldest_student = s
print(f"Самый взрослый студент: {oldest_student['имя']}, возраст {oldest_student['возраст']}, город {oldest_student['город']}")

# Количество студентов, изучающих Python
subject = 'Python'
count_python = 0
for s in students:
    if subject in s['предметы']:
        count_python += 1
print(f"Количество студентов, изучающих {subject}: {count_python}")


# Задание 2: Работа с файлом sales.csv
import csv
from collections import defaultdict

# Чтение данных из файла
sales = []
with open('sales.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Преобразуем сумму в число
        row['Сумма'] = int(row['Сумма'])
        sales.append(row)

# Общая сумма продаж
total_sales = 0
for row in sales:
    total_sales += row['Сумма']
print(f"Общая сумма продаж: {total_sales} руб.")

# Определение продукта с самым высоким объемом продаж
product_sales = defaultdict(int)
for row in sales:
    product_sales[row['Продукт']] += row['Сумма']

best_product_name = None
best_product_sum = -1
for name, total in product_sales.items():
    if total > best_product_sum:
        best_product_sum = total
        best_product_name = name
print(f"Продукт с самыми высокими продажами: {best_product_name} (сумма {best_product_sum} руб.)")

# Разделение по месяцам
monthly_sales = defaultdict(int)
for row in sales:
    # Извлекаем год-месяц из даты (первые 7 символов)
    month = row['Дата'][:7]
    monthly_sales[month] += row['Сумма']
print("Продажи по месяцам:")
for month, amount in sorted(monthly_sales.items()):
    print(f"{month}: {amount} руб.")


# Задание 3: Комбинированная работа с JSON и CSV (employees.json и performance.csv)
import json
import csv

# Чтение сотрудников из JSON
with open('employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)
# Создаем словарь для быстрого доступа по id
emp_dict = {emp['id']: emp for emp in employees}

# Чтение производительности из CSV
performances = []
with open('performance.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        per = {'employee_id': int(row['employee_id']), 'performance': int(row['performance'])}
        performances.append(per)

# Сопоставление данных
for per in performances:
    emp_id = per['employee_id']
    if emp_id in emp_dict:
        emp_dict[emp_id]['performance'] = per['performance']

# Вычисление средней производительности
total_perf = 0
for per in performances:
    total_perf += per['performance']
avg_perf = total_perf / len(performances)
print(f"Средняя производительность среди сотрудников: {avg_perf:.2f}")

# Поиск сотрудника с наивысшей производительностью
best_perf_value = -1
best_perf_record = None
for per in performances:
    if per['performance'] > best_perf_value:
        best_perf_value = per['performance']
        best_perf_record = per
best_emp_id = best_perf_record['employee_id']
best_emp = emp_dict[best_emp_id]
print(f"Сотрудник с наивысшей производительностью: {best_emp['имя']} (показатель {best_perf_value})")



