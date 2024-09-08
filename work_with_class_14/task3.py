import math

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def cercumference(self):
        return 2 * math.pi * self.radius
    
class InscribedCircleInSquare(Square, Circle):
    def __init__(self, side):
        Square.__init__(self, side)
        Circle.__init__(self, side / 2)
    
    def __str__(self):
        return (f"Длина сторон квадрата: {self.side}\nПлощадь квадрата: {self.area()}\nПериметр квадрата: {self.perimeter()}\nРадиус вписаной окружности: {self.radius}\nПлошщадь вписаной окружности: {self.area()}\nДлина окоружности вписаной окружности: {self.cercumference()}")

In_scribed_circle_in_square = InscribedCircleInSquare(10)
print(In_scribed_circle_in_square)