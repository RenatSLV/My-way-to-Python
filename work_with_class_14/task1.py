class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def turn_on (self):
        return f"{self.brand} {self.model} сейчас вкл"
    
    def turn_off(self):
        return f"{self.brand} {self.model} сейчас выкл"
    
    def __str__(self):
        return f"{self.brand} {self.model,}, Сила тока: {self.power}, "
    
class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_contain, coffe_contain):
        super().__init__(brand, model, power)
        self.water_contain = water_contain
        self.coffe_contain = coffe_contain

    def make_coffe(self):
        return "Кофе варится....."
    
    def __str__(self):
        return super().__str__() + f"Объем воды: {self.water_contain}L, Объем кофе: {self.coffe_contain}g"
    
class Blender(Device):
    def __init__(self, brand, model, power, jar_contain, speed):
        super().__init__(brand, model, power)
        self.jar_contain = jar_contain
        self.speed = speed

    def blend(self):
        return f"Ингридиенты перемешиваются..."
    
    def __str__(self):
        return super().__str__() +  f"ОбЪем Ёмкости: {self.jar_contain}L, Скорость: {self.speed}"
    
class MeatGrinder(Device):
    def __init__(self, brand, model, power, Knife):
        super().__init__(brand, model, power)
        self.knife = Knife

    def grinder_meet(self):
        return "Нарезка мяса..."
    
    def __str__(self):
        return super().__str__() + f"Нажы: {self.knife}"
    

coffee_machine = CoffeeMachine("Xiaomi", "CF150", 1500, 2, 300)
print(coffee_machine)
print(coffee_machine.turn_on())
print(coffee_machine.make_coffe())
print(coffee_machine.turn_off())

print(27 * "-")

blender = Blender("Xiaomi", "B450", 1250, 1.2, 5)
print(blender)
print(blender.turn_on())
print(blender.blend())
print(blender.turn_off())

print(27 * "-")

meat_grinder = MeatGrinder("Xiaomi", "MG950", 1900, 8)
print(meat_grinder)
print(meat_grinder.turn_on())
print(meat_grinder.grinder_meet())
print(meat_grinder.turn_off())
