# Абстракция для фигур
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"Drawing a {self.color} shape."

# Конкретные реализации фигур
class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color} circle."

class Square(Shape):
    def draw(self):
        return f"Drawing a {self.color} square."
    
class Rectangle(Shape):
    def draw(self):
        return f"Drawing a {self.color} rectangle."

# Конкретные реализации цветов
class Red:
    def __str__(self):
        return "red"

class Blue:
    def __str__(self):
        return "blue"
    
class Green:
    def __str__(self):
        return "green"

# Пример использования
if __name__ == "__main__":
    red_circle = Circle(Red())
    print(red_circle.draw())

    blue_square = Square(Blue())
    print(blue_square.draw())

    green_rectangle = Rectangle(Green())  # Исправленное имя переменной
    print(green_rectangle.draw())

    red_square = Square(Red())
    print(red_square.draw())

    red_rectangle = Rectangle(Red())  # Исправленное имя переменной
    print(red_rectangle.draw())

    blue_circle = Circle(Blue())
    print(blue_circle.draw())

    blue_rectangle = Rectangle(Blue())  # Исправленное имя переменной
    print(blue_rectangle.draw())

    green_circle = Circle(Green())
    print(green_circle.draw())

    green_square = Square(Green())
    print(green_square.draw())
