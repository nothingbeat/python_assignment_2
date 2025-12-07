class Person:
    """Базовый класс человек"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """Получить личную информацию"""
        return f"Имя: {self.name}, Возраст: {self.age}"


class Student(Person):
    """Класс студента"""

    def __init__(self, name, age, group_number, average_grade):
        super().__init__(name, age)
        self.group_number = group_number
        self.average_grade = average_grade

    def get_scholarship(self):
        """Рассчитать стипендию"""
        if self.average_grade == 5:
            return 6000
        elif self.average_grade >= 4:
            return 4000
        else:
            return 0

    def scholarship_greater_than(self, other):
        """Сравнить, больше ли стипендия"""
        return self.get_scholarship() > other.get_scholarship()

    def get_info(self):
        """Получить информацию о студенте"""
        base_info = super().get_info()
        return f"{base_info}, Номер группы: {self.group_number}, Средний балл: {self.average_grade}"


class GraduateStudent(Person):
    """Класс аспиранта"""

    def __init__(self, name, age, group_number, average_grade, research_work):
        super().__init__(name, age)
        self.group_number = group_number
        self.average_grade = average_grade
        self.research_work = research_work

    def get_scholarship(self):
        """Рассчитать стипендию"""
        if self.average_grade == 5:
            return 8000
        elif self.average_grade >= 4:
            return 6000
        else:
            return 0

    def scholarship_greater_than(self, other):
        """Сравнить, больше ли стипендия"""
        return self.get_scholarship() > other.get_scholarship()

    def get_info(self):
        """Получить информацию об аспиранте"""
        base_info = super().get_info()
        return f"{base_info}, Номер группы: {self.group_number}, Средний балл: {self.average_grade}, Тема исследования: {self.research_work}"


# Тестовый код
if __name__ == "__main__":
    student1 = Student("Чжан Сан", 20, "Группа A", 4.8)
    student2 = Student("Ли Сы", 21, "Группа B", 5.0)
    grad_student = GraduateStudent("Ван У", 25, "Группа C", 4.9, "Исследования в области искусственного интеллекта")

    persons = [student1, student2, grad_student]

    for person in persons:
        print(f"{person.get_info()}, Стипендия: {person.get_scholarship()}元")

    # Сравнение стипендий
    print(f"\nСтипендия {student2.name} больше, чем у {student1.name}: {student2.scholarship_greater_than(student1)}")
    print(f"Стипендия {grad_student.name} больше, чем у {student1.name}: {grad_student.scholarship_greater_than(student1)}")