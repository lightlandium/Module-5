import string

def get_words(filename):
    """
    Читает файл, разбивает текст на слова.
    Приводит все к нижнему регистру, удаляет знаки пунктуации,
    заменяет переводы строк на пробелы.
    Возвращает список слов (с повторениями).
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    # Приводим к нижнему регистру
    text = text.lower()

    # Удаляем знаки пунктуации, заменяя их на пробелы
    # Создаём таблицу перевода: каждый символ пунктуации -> пробел
    # Используем стандартную английскую пунктуацию и добавим русские знаки
    russian_punct = '«»—…“”'
    all_punct = string.punctuation + russian_punct
    translator = str.maketrans(all_punct, ' ' * len(all_punct))
    text = text.translate(translator)

    # Разбиваем текст на слова по пробелам и фильтруем пустые строки
    words = [word for word in text.split() if word]
    return words

def get_words_dict(words):
    """
    Строит словарь частотности слов.
    """
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

def main():
    filename = input("Введите название файла: ").strip() #вводим название hello.txt
    words = get_words(filename)
    if not words:
        return

    words_dict = get_words_dict(words)

    print(f"\nКол-во слов: {len(words)}")
    print(f"Кол-во уникальных слов: {len(words_dict)}")
    print("\nВсе использованные слова:")

    # Выводим слова в алфавитном порядке
    for word in sorted(words_dict.keys()):
        print(word, words_dict[word])

if __name__ == "__main__":
    main()