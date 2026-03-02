# Задача 1, преобразование txt в csv

import csv

def convert_txt_to_csv(input_file='prices.txt', output_file='prices.csv'):
    """
    Читает текстовый файл с табуляцией в качестве разделителя и записывает данные в CSV-файл.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as txt_f:
            lines = txt_f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Подготавливаем данные для записи в CSV
    data = []
    for line in lines:
        line = line.strip()  # убираем лишние пробелы и символы перевода строки
        if not line:  # пропускаем пустые строки
            continue
        # Разделяем по символу табуляции
        parts = line.split('\t')
        if len(parts) != 3:
            print(f"Предупреждение: строка '{line}' имеет неверный формат и будет пропущена.")
            continue
        name, quantity, price = parts
        # Проверяем, что количество и цена — целые числа (можно добавить проверку)
        try:
            quantity = int(quantity)
            price = int(price)
        except ValueError:
            print(f"Предупреждение: в строке '{line}' количество или цена не являются целыми числами. Строка пропущена.")
            continue
        data.append([name, quantity, price])

    # Записываем в CSV
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as csv_f:
            writer = csv.writer(csv_f)
            writer.writerows(data)
        print(f"Данные успешно сохранены в файл {output_file}")
    except Exception as e:
        print(f"Ошибка при записи CSV: {e}")

if __name__ == '__main__':
    convert_txt_to_csv()

# Задача 2, подсчет стоимости заказа из prices.csv
import csv

def calculate_total_cost(input_file='prices.csv'):
    """
    Читает CSV-файл с колонками: наименование, количество, цена за штуку.
    Возвращает общую стоимость заказа.
    """
    total = 0
    try:
        with open(input_file, 'r', encoding='utf-8') as csv_f:
            reader = csv.reader(csv_f)
            for row in reader:
                if len(row) != 3:
                    print(f"Предупреждение: строка {row} имеет неверный формат и будет пропущена.")
                    continue
                name, quantity_str, price_str = row
                try:
                    quantity = int(quantity_str)
                    price = int(price_str)
                except ValueError:
                    print(f"Предупреждение: в строке {row} количество или цена не являются целыми числами. Строка пропущена.")
                    continue
                item_total = quantity * price
                total += item_total
                print(f"{name}: {quantity} шт. × {price} руб. = {item_total} руб.")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

    return total

if __name__ == '__main__':
    total_cost = calculate_total_cost()
    if total_cost is not None:
        print(f"\nОбщая стоимость заказа: {total_cost} руб.")