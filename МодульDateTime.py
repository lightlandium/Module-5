from datetime import datetime, date, time, timedelta
import calendar

# Часть 1: Работа с текущей датой и временем
# Получаем текущие дату и время
now = datetime.now()
print(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Выводим день недели
weekday = now.strftime('%A')
print(f"День недели: {weekday}")

# Определяем, високосный ли год
year = now.year
if calendar.isleap(year):
    print(f"Год {year} високосный.")
else:
    print(f"Год {year} не високосный.")

print()

# Часть 2: Работа с пользовательской датой

# Запрашиваем дату у пользователя
user_input = input("Введите дату в формате ГГГГ-ММ-ДД (например, 2025-12-31): ")

try:
    # Преобразуем строку в объект date
    user_date = datetime.strptime(user_input, "%Y-%m-%d").date()
except ValueError:
    print("Ошибка: неверный формат даты. Завершение программы.")
    exit()

# Текущая дата (без времени)
today = date.today()

# Вычисляем разницу в днях
delta_days = (user_date - today).days

if delta_days > 0:
    print(f"До введённой даты осталось {delta_days} дн.")
elif delta_days < 0:
    print(f"Введённая дата была {abs(delta_days)} дн. назад.")
else:
    print("Введённая дата — сегодня!")

user_datetime = datetime.combine(user_date, time.min)
now_datetime = datetime.now()

# Разница
diff = user_datetime - now_datetime

# Извлекаем дни, секунды и преобразуем в часы и минуты
days = diff.days
seconds = diff.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60

# Выводим результат
if days >= 0:
    print(f"До указанной даты осталось: {days} дн., {hours} ч., {minutes} мин.")
else:
    print(f"С указанной даты прошло: {abs(days)} дн., {hours} ч., {minutes} мин.")