import os
import shutil

# Часть 1: Работа с файлами и директориями

# Создаем новую директорию "Управление_файлами"
dir_name = "Управление_файлами"
os.makedirs(dir_name, exist_ok=True)  # exist_ok=True чтобы не было ошибки, если директория уже существует

# Создаем два файла в этой директории
file1_path = os.path.join(dir_name, "file1.txt")
file2_path = os.path.join(dir_name, "file2.txt")

# Записываем текст в файлы
with open(file1_path, "w", encoding="utf-8") as f:
    f.write("Это текст первого файла.\n")

with open(file2_path, "w", encoding="utf-8") as f:
    f.write("Это текст второго файла.\n")

# Выводим содержимое директории
print("Содержимое директории 'Управление_файлами' после создания файлов:")
for item in os.listdir(dir_name):
    print(item)

# Часть 2: Удаление файлов и директории

# Удаляем один из файлов
os.remove(file1_path)
print(f"\nФайл {file1_path} удален.")

# Создаем поддиректорию внутри "Управление_файлами"
subdir_name = os.path.join(dir_name, "поддиректория")
os.makedirs(subdir_name, exist_ok=True)

# Перемещаем оставшийся файл (file2.txt) в поддиректорию
new_file_path = os.path.join(subdir_name, "file2.txt")
shutil.move(file2_path, new_file_path)
print(f"Файл file2.txt перемещен в {subdir_name}")

# Удаляем исходную директорию "Управление_файлами" вместе со всем содержимым
shutil.rmtree(dir_name)
print(f"Директория '{dir_name}' и все её содержимое удалены.")