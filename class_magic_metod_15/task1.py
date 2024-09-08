import math

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
    
    def circle_len(self):
        return self.radius * math.pi * 2
    
    def __eq__(self, other):
        return self.radius == other.radius  # ==
    
    def __lt__(self, other):
        return self.circle_len() < other.circle_len() # <
    
    def __gt__(self, other):
        return self.circle_len() > other.circle_len() # >
    
    def __le__(self, other):
        return self.circle_len() <= other.circle_len() # <=
    
    def __ge__(self, other):
        return self.circle_len() >= other.circle_len() # >=
    
    def __add__(self, num: int):
        return Circle(self.radius + num) # +
    
    def __sub__(self, num: int):
        return Circle(self.radius - num) # -
    
    def __iadd__(self, num: int):
        self.radius += num # +=
        return self
    
    def __isub__(self, num: int):
        self.radius -= num # -=
        return self
    
    def __repr__(self):
        return f"radius = {self.radius}"
    
c1 = Circle(int(input("Введите число для радиуса: ")))
c2 = Circle(int(input("Введите число для радиуса: ")))

#сравнение
print(c1 == c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)

print(27 * "-")
#операции + - += -=
print(c1 + 3)
print(c1 - 3)
c1 += 3
print(c1)
c1 -= 3
print(c1)

print(27 * "-")

print(c2 + 5)
print(c2 - 5)
c2 += 5
print(c1)
c2 -= 5
print(c1)