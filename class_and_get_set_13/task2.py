class Book:
    def __init__(self, name, year, publisher, genre, creater, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.creater = creater
        self.price = price
    
    def input_value(self):
        self.name = input("Введите название: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите название издателя: ")
        self.genre = input("Введите жанр: ")
        self.creater = input("Введите Автора: ")
        self.price = int(input("Введите цену: "))
    
    def display_value(self):
        print(f"название: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель : {self.publisher}")
        print(f"Жанр : {self.genre}")
        print(f"Автор: {self.creater}")
        print(f"Цена: {self.price} в тенге")
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year
    def set_year(self, year):
        self.year = year

    def get_publisher(self):
        return self.publisher
    def set_pumlisher(self, publisher):
        self.publisher = publisher

    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre
    
    def get_creater(self):
        return self.creater
    def set_creater(self, creater):
        self.creater = creater

    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    
book = Book("Хребты безумия", 2019, "pocketbook", "Фантастика", "Говард Лафкрафт", 990)

# book.input_value()
# print(27 * "-")
# book.display_value()

print(f"Название: {book.get_name()}")
book.set_name("Ктулху")
print(f"Обновленное название: {book.get_name()}")