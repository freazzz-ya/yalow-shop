nums = [i for i in range(1, 34)]
values = [chr(i + 1072) for i in range(1, 34)]
generate_dict = {key: value for key, value in zip(nums, values)}
from functools import wraps


def decor(exclude: list):
    def debug(func):
        @wraps(func)
        def wrapper(*args, **kwargs: dict):
            if exclude in kwargs:
                pass
            print(func.__name__)
            print(args)
            print(kwargs)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return debug






# Открываем файл для записи
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Открываем файл для чтения
with open("example.txt", "r") as file:
    # Позиция курсора в начале файла (должна быть 0)
    position = file.tell()
    print("Current position:", position)

    # Читаем первую строку
    first_line = file.readline()
    print("First line:", first_line)

    # Позиция курсора после чтения первой строки
    position = file.tell()
    print("Current position after reading the first line:", position)

    # Перемещаем курсор обратно в начало файла
    file.seek(0)

    # Снова считываем содержимое файла
    content = file.read()
    print("File content after seeking back to the beginning:")
    print(content)