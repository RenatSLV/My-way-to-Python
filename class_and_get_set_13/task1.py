class Cars:
    def __init__(self,name_modal, years, make_company, engine_capacity, color, price):
        self.name_modal = name_modal
        self.years = years
        self.make_company = make_company
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
    
    def input_value(self):
        self.name_modal = input("Введите модель: ")
        self.years = int(input("Введите год выпуска: "))
        self.make_company = input("Введите название компаний: ")
        self.engine_capacity = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет: ")
        self.price = int(input("Введите цену: "))
    
    def display_value(self):
        print(f"Модель: {self.name_modal}")
        print(f"Год выпуска: {self.years}")
        print(f"Комания : {self.make_company}")
        print(f"Объем двигателя : {self.engine_capacity} в литрах")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} в тенге")
    
    def get_model(self):
        return self.name_modal
    def set_model(self, name_modal):
        self.name_modal = name_modal
    
    def get_year(self):
        return self.years
    def set_year(self, year):
        self.years = year
    
    def get_company(self):
        return self.make_company
    def set_company(self, company):
        self.make_company = company

    def get_engine_value(self):
        return self.engine_capacity
    def set_engine_value(self, engine_value):
        self.engine_capacity = engine_value
    
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price

car = Cars("BMW E38", 2001, "BMW company", 4.4, "Black", 750000)

car.input_value()
print(27 * "-")
car.display_value()

# print(f"Модель: {car.get_model()}")
# car.set_model("BMW E39")
# print(f"Обновленное название: {car.get_model()}")
