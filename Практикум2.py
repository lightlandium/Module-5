from collections import Counter, namedtuple, defaultdict, deque
import random

# Задание 1
numbers = [random.randint(1, 10) for _ in range(20)]
print("Сгенерированный список:", numbers)

counter = Counter(numbers)
print(f"Количество уникальных элементов: {len(counter)}")

most_common_three = counter.most_common(3)
print("Три самых частых элемента:")
for elem, count in most_common_three:
    print(f"  {elem} встречается {count} раз(а)")
print ()

# Задание 2
# Создаём кортеж Book
Book = namedtuple('Book', ['title', 'author', 'genre'])

# Создаём несколько экземпляров
book1 = Book('Война и мир', 'Лев Толстой', 'Роман')
book2 = Book('1984', 'Джордж Оруэлл', 'Антиутопия')
book3 = Book('Мастер и Маргарита', 'Михаил Булгаков', 'Роман')

# Выводим информацию о книгах, используя атрибуты
print("Информация о книгах:")
print(f"Книга 1: {book1.title}, автор: {book1.author}, жанр: {book1.genre}")
print(f"Книга 2: {book2.title}, автор: {book2.author}, жанр: {book2.genre}")
print(f"Книга 3: {book3.title}, автор: {book3.author}, жанр: {book3.genre}")
print()

# Задание 3
dd = defaultdict(list)

dd['фрукты'].append('яблоко')
dd['фрукты'].append('банан')
dd['овощи'].append('морковь')
dd['фрукты'].append('апельсин')
dd['овощи'].append('помидор')
dd['ягоды'].append('клубника')

print("Содержимое defaultdict (ключи со списками значений):")
for key, values in dd.items():
    print(f"{key}: {values}")
print()

# Задание 4
dq = deque([1, 2, 3])
print("Исходный deque:", list(dq))

# Добавляем в конец
dq.append(4)
print("После append(4):", list(dq))

# Добавляем в начало
dq.appendleft(0)
print("После appendleft(0):", list(dq))

# Удаляем с конца
last = dq.pop()
print(f"После pop() (удалён {last}):", list(dq))

# Удаляем с начала
first = dq.popleft()
print(f"После popleft() (удалён {first}):", list(dq))
print()

# Задание 5
def enqueue(queue, item):
    """Добавляет элемент в конец очереди."""
    queue.append(item)

def dequeue(queue):
    """Извлекает элемент из начала очереди. Если очередь пуста, возвращает None."""
    if queue:
        return queue.popleft()
    else:
        print("Очередь пуста")
        return None

queue = deque()

enqueue(queue, 'a')
enqueue(queue, 'b')
enqueue(queue, 'c')
print("Очередь после добавления элементов:", list(queue))

print("Извлечено:", dequeue(queue))
print("Очередь после извлечения:", list(queue))
print("Извлечено:", dequeue(queue))
print("Очередь после извлечения:", list(queue))
print("Извлечено:", dequeue(queue))
print("Очередь после извлечения:", list(queue))

print("Извлечено:", dequeue(queue))