class Ship:
    def __init__(self, name, height, width, length):
        self.height = height
        self.width = width
        self.length = length
        self.name = name

    def go_in_ocean(self):
        return f"Корабль '{self.name}' отпроаляется в океан"
    
    def go_back(self):
        return f"Корабль '{self.name}' прибыл в порт"

    def __str__(self):
        return f"Название коробля: {self.name}\nВысота Коробля: {self.height}m\nШирина Коробля: {self.width}m \nДлина Коробля: {self.length}m\n"
    
class Frigate(Ship):
    def __init__(self, name, height, width, length, title, crew):
        super().__init__(name, height, width, length)
        self.title = title
        self.crew = crew
    
    def ship_go_to_trip(self):
        return f"Корабль отправился в путишествие"

    def __str__(self):
        return super().__str__() + f"Титул: {self.title}\nЭкипаж: {self.crew}"
    
class Destroyer(Ship):
    def __init__(self, name, height, width, length, title, crew):
        super().__init__(name, height, width, length)
        self.title = title
        self.crew = crew
    
    def ship_go_to_trip(self):
        return f"Корабль отправился в путишествие"

    def __str__(self):
        return super().__str__() + f"Титул: {self.title}\nЭкипаж: {self.crew}"
    
class Cruiser(Ship):
    def __init__(self, name, height, width, length, title, crew):
        super().__init__(name, height, width, length)
        self.title = title
        self.crew = crew
    
    def ship_go_to_trip(self):
        return f"Корабль отправился в путишествие"

    def __str__(self):
        return super().__str__() + f"Титул: {self.title}\nЭкипаж: {self.crew}"
    
frigate = Frigate("Звезда", 10, 5, 20, "Королевский", "Полный 20 чел.")
print(frigate)
print(frigate.go_in_ocean())
print(frigate.go_back())
print(frigate.ship_go_to_trip())

print(27 * "-")

destroyer = Destroyer("Мария", 15, 10, 30, "Пиратский", "Неизвестно")
print(destroyer)
print(destroyer.go_in_ocean())
print(destroyer.go_back())
print(destroyer.ship_go_to_trip())

print(27 * "-")

сruiser = Cruiser("Белый Кит", 50, 45, 250, "Частный", "Полный 150 чел")
print(сruiser)
print(сruiser.go_in_ocean())
print(сruiser.go_back())
print(сruiser.ship_go_to_trip())