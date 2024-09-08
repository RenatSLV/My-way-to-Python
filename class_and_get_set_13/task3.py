class Stadium:
    def __init__(self, name, date_opening, country, town, contain):
        self.name = name
        self.date_opening = date_opening
        self.country = country
        self.town = town
        self.contain = contain

    def input_value(self):
        self.name = input("Введите название стадиона: ")
        self.date_opening = int(input("Введите дату открытия: "))
        self.country = input("введите строну: ")
        self.town = input("Введите город: ")
        self.contain = int(input("Введите вмeстимость"))

    def display_value(self):
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытие: {self.date_opening}")
        print(f"Навание строны: {self.country}")
        print(f"Название города: {self.town}")
        print(f"Вместимость стадиона: {self.contain}")

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_date_opening(self):
        return self.date_opening
    def set_date_opening(self, date_opening):
        self.date_opening = date_opening

    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    
    def get_town(self):
        return self.town
    def set_town(self, town):
        self.town = town

    def get_contain(self):
        return self.contain
    def set_contain(self, contain):
        self.contain = contain

stadium = Stadium("Энфилд", 1884, "Англия", "Ливерпуль", 61217)

# stadium.input_value()
# print(27 * "-")
# stadium.display_value()

print(f"Название стадиона: {stadium.get_name()}")
stadium.set_name("Бруклин")
print(f"Обновленное название: {stadium.get_name()}")