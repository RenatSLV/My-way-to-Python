class Wheels:
    def __init__(self, wheels: int) -> str:
        self.wheels = wheels

    def show_wheels(self):
        return f"Колёс: {self.wheels} Шт."
    
class Engine:
    def __init__(self, engine: int) -> str:
        self.engine = engine

    def show_engine(self):
        return f"Двигатель: {self.engine} Шт."
    
class Doors:
    def __init__(self, doors: int) -> str:
        self.doors = doors

    def show_doors(self):
        return f"Двери: {self.doors} Шт."
    

class Car(Wheels, Engine, Doors):
    def __init__(self, wheels, engine, doors):
        Wheels.__init__(self, wheels)
        Engine.__init__(self, engine)
        Doors.__init__(self, doors)

    def __str__(self):
        return f"В машине есть {self.show_wheels()}\nВ машине есть {self.show_engine()}\nВ машине есть {self.show_doors()}"
    
car = Car(4, 1, 5)
print(car)
