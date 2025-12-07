def filter_strings(filter_func, string_array):
    """
    Отфильтровать массив строк с помощью лямбда-функции

    Args:
        filter_func: Фильтрующая функция
        string_array: Массив строк

    Returns:
        list: Отфильтрованный массив
    """
    return list(filter(filter_func, string_array))

# Тестовый код
if __name__ == "__main__":
    strings = ["apple", "banana", "a test", "hello world", "cat", "elephant"]

    # 1. Исключить строки, содержащие пробелы
    no_spaces = filter_strings(lambda s: ' ' not in s, strings)
    print("Без пробелов:", no_spaces)

    # 2. Исключить строки, начинающиеся на 'a'
    no_a_start = filter_strings(lambda s: not s.startswith('a'), strings)
    print("Не начинаются на 'a':", no_a_start)

    # 3. Исключить строки короче 5 символов
    min_length_5 = filter_strings(lambda s: len(s) >= 5, strings)
    print("Длина >= 5:", min_length_5)