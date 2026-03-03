import itertools
import math

def create_deck():
    """Создаёт стандартную колоду из 52 карт."""
    suits = ['червы', 'бубны', 'трефы', 'пики']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    return deck

def main():
    deck = create_deck()
    print("Колода готова. Всего карт:", len(deck))

    # Ввод количества карт в комбинации
    try:
        k = int(input("Введите количество карт в комбинации (от 1 до 52): "))
        if k < 1 or k > 52:
            print("Ошибка: число должно быть от 1 до 52.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    # Количество комбинаций
    total = math.comb(52, k)
    print(f"Всего комбинаций из {k} карт: {total}")

    if total == 0:
        print("Нет комбинаций.")
        return

    # Если комбинаций слишком много, предложим сохранить в файл
    if total > 1000:
        answer = input("Комбинаций слишком много. Вывести на экран? (y/n, по умолчанию сохранение в файл): ").lower()
        if answer != 'y':
            filename = f"combinations_{k}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                # Используем itertools.combinations для генерации
                for i, comb in enumerate(itertools.combinations(deck, k), 1):
                    f.write(f"{i}: {', '.join(comb)}\n")
            print(f"Комбинации сохранены в файл {filename}")
            return

    # Выводим на экран
    print("\nВсе комбинации:")
    for i, comb in enumerate(itertools.combinations(deck, k), 1):
        print(f"{i}: {', '.join(comb)}")

if __name__ == "__main__":
    main()