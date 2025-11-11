import time
import functools

def timer_decorator(func):
    """Декоратор для измерения времени выполнения функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
        return result
    return wrapper

# Первая тестовая функция: вычисление суммы двух чисел
@timer_decorator
def add_numbers(a, b):
    """Вычислить сумму двух чисел"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# Вторая тестовая функция: операции чтения/записи файлов
@timer_decorator
def file_operations(input_file, output_file):
    """Считать два числа из файла, вычислить их сумму и записать в выходной файл"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            numbers = f.read().strip().split()
            if len(numbers) >= 2:
                a = float(numbers[0])
                b = float(numbers[1])
                result = a + b

                with open(output_file, 'w', encoding='utf-8') as out_f:
                    out_f.write(f"{a} + {b} = {result}")

                print(f"Результат записан в файл: {output_file}")
                return result
            else:
                print("Ошибка формата входного файла")
                return None
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return None
    except ValueError:
        print("Ошибка формата содержимого файла")
        return None

# Тестовый код
if __name__ == "__main__":
    # Тест первой функции
    print("Тест функции сложения:")
    add_numbers(123456, 654321)

    print("\nТест функции работы с файлами:")
    # Создать тестовый входной файл
    with open('input.txt', 'w', encoding='utf-8') as f:
        f.write("10 20")

    file_operations('input.txt', 'output.txt')

    # Показать содержимое выходного файла
    try:
        with open('output.txt', 'r', encoding='utf-8') as f:
            print(f"Содержимое выходного файла: {f.read()}")
    except FileNotFoundError:
        print("Выходной файл не создан")