import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """Абстрактный базовый класс: геометрическая фигура"""

    @abstractmethod
    def area(self):
        """Вычислить площадь"""
        pass

    @abstractmethod
    def perimeter(self):
        """Вычислить периметр"""
        pass

    def area_greater_than(self, other):
        """Сравнить, больше ли площадь, чем у другой фигуры"""
        return self.area() > other.area()

    def perimeter_greater_than(self, other):
        """Сравнить, больше ли периметр, чем у другой фигуры"""
        return self.perimeter() > other.perimeter()


class Square(Shape):
    """Квадрат"""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Square(side={self.side})"


class Rectangle(Shape):
    """Прямоугольник"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


class Triangle(Shape):
    """Треугольник"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Формула Герона
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


class Circle(Shape):
    """Круг"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


# Тестовый код
if __name__ == "__main__":
    shapes = [
        Square(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Circle(3)
    ]

    for shape in shapes:
        print(f"{shape}: площадь={shape.area():.2f}, периметр={shape.perimeter():.2f}")

    # Тест сравнения
    square = Square(4)
    circle = Circle(2)
    print(f"\nПлощадь квадрата > площади круга: {square.area_greater_than(circle)}")
    print(f"Периметр квадрата > периметра круга: {square.perimeter_greater_than(circle)}")