import telebot
from datetime import datetime
import json
import os
import sys

# 1. Безопасная загрузка токена 
TOKEN = os.getenv('TG_TOKEN')
if TOKEN is None:
    print("Ошибка: переменная окружения TG_TOKEN не задана.")
    print("Установите токен бота и перезапустите программу.")
    sys.exit(1)
else:
    # Не выводим токен в консоль, только факт загрузки
    print("Токен загружен")

bot = telebot.TeleBot(TOKEN)

# Временное хранилище для пользователей, которые отметили /sleep, но ещё не /wake
sleep_times = {}

# Основное хранилище данных: для каждого пользователя хранится список его записей о сне
sleep_data = {}  # формат: {user_id: [запись1, запись2, ...]}

DATA_FILE = 'sleep_data.json'


def load_data():
    global sleep_data
    try:
        if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)

            # Фильтруем записи с корректными datetime
            cleaned_data = {}
            for user_id, records in loaded_data.items():
                valid_records = []
                for record in records:
                    # Проверяем наличие обоих полей
                    if 'start_time' not in record or 'wake_time' not in record:
                        print(f"Пропущена запись для {user_id}: отсутствует start_time или wake_time")
                        continue

                    # Преобразуем строки в datetime
                    try:
                        start_time = datetime.fromisoformat(record['start_time'])
                        wake_time = datetime.fromisoformat(record['wake_time'])
                    except (ValueError, TypeError) as e:
                        print(f"Ошибка преобразования datetime для {user_id}: {e}")
                        continue  # пропускаем всю запись целиком

                    # Валидная запись – копируем с корректными datetime
                    valid_record = {
                        'start_time': start_time,
                        'wake_time': wake_time,
                        'duration': record.get('duration', 0.0)
                    }
                    if 'quality' in record:
                        valid_record['quality'] = record['quality']
                    if 'notes' in record:
                        valid_record['notes'] = record['notes']

                    valid_records.append(valid_record)

                if valid_records:
                    cleaned_data[user_id] = valid_records

            sleep_data = cleaned_data
            print(f"Загружено данных для {len(sleep_data)} пользователей")
        else:
            print("Файл данных не найден или пуст, начинаем с чистого листа")
            sleep_data = {}
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        sleep_data = {}


def save_data():
    try:
        data_to_save = {}
        for user_id, records in sleep_data.items():
            records_copy = []
            for record in records:
                record_copy = record.copy()
                if 'start_time' in record_copy and isinstance(record_copy['start_time'], datetime):
                    record_copy['start_time'] = record_copy['start_time'].isoformat()
                if 'wake_time' in record_copy and isinstance(record_copy['wake_time'], datetime):
                    record_copy['wake_time'] = record_copy['wake_time'].isoformat()
                records_copy.append(record_copy)
            data_to_save[user_id] = records_copy

        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)
        print("Данные успешно сохранены")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")


load_data()


@bot.message_handler(commands=['start'])
def start(message):
    text = """Привет! Я бот для отслеживания сна.

Команды:
/sleep - отметить время отхода ко сну
/wake - отметить время пробуждения
/stats - показать статистику сна
/clear - очистить данные о сне

Как использовать:
1. Вечером отправьте /sleep
2. Утром отправьте /wake
3. Оцените качество сна (1-10)
4. При желании добавьте заметки"""

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['sleep'])
def sleep_start(message):
    user_id = str(message.from_user.id)
    current_time = datetime.now()
    sleep_times[user_id] = current_time
    bot.send_message(message.chat.id,
                     f"Зафиксировано время отхода ко сну: {current_time.strftime('%H:%M')}\nУтром отправьте /wake")


@bot.message_handler(commands=['wake'])
def sleep_end(message):
    user_id = str(message.from_user.id)
    wake_time = datetime.now()

    if user_id not in sleep_times:
        bot.send_message(message.chat.id, "Вы не отмечали отход ко сну командой /sleep")
        return

    sleep_time = sleep_times.pop(user_id)

    duration_seconds = (wake_time - sleep_time).total_seconds()
    if duration_seconds < 0:
        bot.send_message(message.chat.id, "Ошибка: время пробуждения раньше времени засыпания!")
        return

    duration = duration_seconds / 3600

    new_record = {
        'start_time': sleep_time,
        'wake_time': wake_time,
        'duration': round(duration, 2)
    }

    if user_id not in sleep_data:
        sleep_data[user_id] = []
    sleep_data[user_id].append(new_record)

    msg = bot.send_message(message.chat.id,
                           f"Продолжительность сна: {duration:.1f} часов\n\nОцените качество сна от 1 до 10:")
    bot.register_next_step_handler(msg, ask_quality, user_id, len(sleep_data[user_id]) - 1)


def ask_quality(message, user_id, record_index):
    try:
        quality = int(message.text)
        if 1 <= quality <= 10:
            sleep_data[user_id][record_index]['quality'] = quality
            msg = bot.send_message(message.chat.id, "Добавьте заметки о сне (или отправьте '-' для пропуска):")
            bot.register_next_step_handler(msg, ask_notes, user_id, record_index)
        else:
            msg = bot.send_message(message.chat.id, "Пожалуйста, введите число от 1 до 10:")
            bot.register_next_step_handler(msg, ask_quality, user_id, record_index)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Пожалуйста, введите число от 1 до 10:")
        bot.register_next_step_handler(msg, ask_quality, user_id, record_index)


def ask_notes(message, user_id, record_index):
    notes = message.text
    if notes.strip() and notes.strip() != '-':
        sleep_data[user_id][record_index]['notes'] = notes.strip()

    save_data()

    record = sleep_data[user_id][record_index]
    response = "Данные сохранены!\n\n"
    response += f"Время отхода ко сну: {record['start_time'].strftime('%H:%M')}\n"
    response += f"Время пробуждения: {record['wake_time'].strftime('%H:%M')}\n"
    response += f"Продолжительность: {record['duration']} часов\n"

    if 'quality' in record:
        response += f"Качество сна: {record['quality']}/10\n"

    if 'notes' in record:
        response += f"Заметки: {record['notes']}"

    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['stats'])
def show_stats(message):
    user_id = str(message.from_user.id)

    if user_id not in sleep_data or not sleep_data[user_id]:
        bot.send_message(message.chat.id, "У вас нет сохраненных данных о сне")
        return

    last_record = sleep_data[user_id][-1]

    response = "Ваша статистика сна (последняя запись):\n\n"
    response += f"Время отхода: {last_record['start_time'].strftime('%H:%M %d.%m.%Y')}\n"
    response += f"Время пробуждения: {last_record['wake_time'].strftime('%H:%M %d.%m.%Y')}\n"
    response += f"Продолжительность: {last_record['duration']} часов\n"

    if 'quality' in last_record:
        response += f"Качество: {last_record['quality']}/10\n"

    if 'notes' in last_record and last_record['notes']:
        response += f"Заметки: {last_record['notes']}\n"

    if last_record['duration'] < 6:
        response += "\nСлишком короткий сон! Рекомендуется 7-9 часов."
    elif last_record['duration'] > 10:
        response += "\nСлишком долгий сон! Возможно, вы пересыпаете."
    else:
        response += "\nПродолжительность сна в норме!"

    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['clear'])
def clear_data(message):
    user_id = str(message.from_user.id)

    if user_id in sleep_data:
        del sleep_data[user_id]
        save_data()
        bot.send_message(message.chat.id, "Данные о сне очищены")
    else:
        bot.send_message(message.chat.id, "У вас нет сохраненных данных")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text.lower() in ['помощь', 'help']:
        start(message)
    else:
        bot.send_message(message.chat.id, "Используйте команды из меню или /start для помощи")


print("Бот для отслеживания сна запущен!")
try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Ошибка при запуске бота: {e}")
