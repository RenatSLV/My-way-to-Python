import json

class Shape:
    def __init__(self):
        pass

    def show(self):
        raise NotImplementedError("Нужно реализовать метод в подклассе")
    
    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.__dict__, f)

    def load(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.__dict__.update(data)

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(f"Квадрат: верхний левый угол ({self.x},{self.y}) Длина сторон: {self.side}")
    
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def show(self):
        print(f"Прямоугольник: верхний левый угол ({self.x},{self.y}) Ширина: {self.width} Высота: {self.height}")

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        print(f"Окружность: Центр ({self.center_x},{self.center_y}) Радиус: {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def show(self):
        print(f"Эллипса: верхний левый угол ({self.x},{self.y}) Ширина: {self.width} Высота: {self.height}")

#список фигур
shapes = [
    Square(1, 1, 4),
    Rectangle(2, 2, 5, 6),
    Circle(5, 5, 3),
    Ellipse(6, 6, 7, 8)
]

#Сохраняем фигуры в файл
for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.json')

#Загружаем фигуры в новый список
loaded_shapes = []
for i in range(len(shapes)):
    with open(f'shape_{i}.json', 'r') as f:
        data = json.load(f)
        if 'side' in data:
            loaded_shape = Square(data['x'], data['y'], data['side'])
        elif 'width' in data and 'height' in data:
            if 'center_x' in data:
                loaded_shape = Ellipse(data['x'], data['y'], data['width'], data['height'])
            else:
                loaded_shape = Rectangle(data['x'], data['y'], data['width'], data['height'])
        elif 'radius' in data:
            loaded_shape = Circle(data['center_x'], data['center_y'], data['radius'])
        loaded_shapes.append(loaded_shape)

#Выводим информацию о каждой фигуре
for shape in loaded_shapes:
    shape.show()