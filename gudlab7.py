from functools import partial


# Функция для чтения данных из файла
def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()


# Функция для удаления символа новой строки из строк
def strip_newline(s):
    return s.strip()


# Функция для преобразования строк в целые числа
def str_to_int(s):
    return int(s)


# Функция для фильтрации данных
def filter_data(data, threshold):
    return filter(lambda x: x > threshold, data)


# Функция для вывода данных
def print_data(data):
    for item in data:
        print(item)


# Композиция функций для обработки данных
def process_data(filename, threshold):
    data = read_file(filename)
    data = map(strip_newline, data)
    data = map(str_to_int, data)
    data = filter_data(data, threshold)
    print_data(data)


# Пример использования
if __name__ == "__main__":
    filename = 'data.txt'
    threshold = 10
    process_data(filename, threshold)
