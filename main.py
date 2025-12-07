def main():
    print("=== Демонстрация Python Assignment 2 ===\n")

    # Демонстрация задачи 1
    print("Задача 1: Проверка палиндромов")
    from task1.palindrome import is_palindrome
    test_strings = ["radar", "hello", "A man a plan a canal Panama"]
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")
    print()

    # Демонстрация задачи 2
    print("Задача 2: Фильтрация с помощью lambda")
    from task2.filter_lambda import filter_strings
    strings = ["apple", "a test", "hello world", "cat", "elephant"]
    filtered = filter_strings(lambda s: len(s) >= 5, strings)
    print(f"Результат фильтрации: {filtered}")
    print()

    # Демонстрация задачи 3
    print("Задача 3: Геометрические фигуры")
    from task3.shapes import Square, Circle
    square = Square(5)
    circle = Circle(3)
    print(f"Квадрат: площадь={square.area()}, периметр={square.perimeter()}")
    print(f"Круг: площадь={circle.area():.2f}, периметр={circle.perimeter():.2f}")
    print()

    # Демонстрация задачи 4
    print("Задача 4: Система управления студентами")
    from task4.students import Student, GraduateStudent
    student = Student("Сяо Мин", 20, "CS101", 4.8)
    grad = GraduateStudent("Доктор", 25, "PHD001", 5.0, "Машинное обучение")
    print(student.get_info())
    print(grad.get_info())
    print()

    # Демонстрация задачи 5
    print("Задача 5: Тест декоратора")
    from task5.timer_decorator import add_numbers
    add_numbers(100, 200)


if __name__ == "__main__":
    main()