class Airplane:
    def __init__(self, class_airplans: str, contain: int, max_contain: int):
        self.class_airplans = class_airplans
        self.contain = contain
        self.max_contain = max_contain

    def __eq__(self, other):
        return self.class_airplans == other.class_airplans # ==
    
    def __lt__(self, other):
        return self.max_contain < other.max_contain # <
    
    def __gt__(self, other):
        return self.max_contain > other.max_contain # >
    
    def __le__(self, other):
        return self.max_contain <= other.max_contain # <=
    
    def __ge__(self, other):
        return self.max_contain >= other.max_contain # >=
    
    def __add__(self, num: int):
        return self.contain + num # +
    
    def __sub__(self, num: int):
        return self.contain - num # -
    
    def __iadd__(self, num: int):
        self.contain += num # +=
        return self
    
    def __isub__(self, num: int):
        self.contain -= num # -=
        return self
    
    def __repr__(self):
        return f"Вместимость = {self.contain}"
    
air1 = Airplane("class A", 150, 200)
air2 = Airplane("class A", 100, 150)

print(air1 == air2)
print(air1 < air2)
print(air1 > air2)
print(air1 <= air2)
print(air1 >= air2)

print(air1 + 20)
print(air2 - 20)

air1 += 100
print(air1)

air2 -= 10
print(air2)