import csv
import json


def convert_csv_to_json(csv_filename, delimiter=','):
    """
    Читает CSV-файл и преобразует его в список словарей.
    Первая строка файла считается заголовком (названия колонок).
    Возвращает список словарей {колонка: значение} или None при ошибке.
    """
    data = []
    try:
        with open(csv_filename, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Ошибка: файл '{csv_filename}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

    return data


def main():
    # Запрашиваем имя файла
    filename = input("Введите имя CSV-файла: ").strip()
    if not filename:
        print("Ошибка: имя файла не может быть пустым.")
        return

    delim = input("Введите разделитель столбцов (по умолчанию ','): ").strip()
    if not delim:
        delim = ','

    # Выполняем конвертацию
    result = convert_csv_to_json(filename, delimiter=delim)
    if result is None:
        return

    # Выводим JSON с отступами 4
    json_str = json.dumps(result, ensure_ascii=False, indent=4)
    print("\nРезультат в формате JSON:\n")
    print(json_str)


if __name__ == "__main__":
    main()
