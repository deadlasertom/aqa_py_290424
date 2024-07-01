from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.141595 * self.radius ** 2


if __name__ == "__main__":
    square = Square(5)
    print("Площа квадрата:", square.area())
    circle = Circle(3)
    print("Площа кола:", circle.area())
