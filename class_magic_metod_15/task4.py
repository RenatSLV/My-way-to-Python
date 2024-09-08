class Flat:
    def __init__(self, width: int, light: int, price: int):
        self.width = width
        self.light = light
        self.price = price

    def s_flat(self):
        return self.width * self.light

    def __eq__(self, other):
        return self.s_flat() == other.s_flat() # ==
    
    def __ne__(self, other):
        return self.s_flat() != other.s_flat() # !=
    
    def __lt__(self, other):
        return self.price < other.price # <
    
    def __gt__(self, other):
        return self.price > other.price # >
    
    def __le__(self, other):
        return self.price <= other.price # <=
    
    def __ge__(self, other):
        return self.price >= other.price # >=
    
    
flat1 = Flat(150, 100, 250000)
flat2 = Flat(200, 250, 350000)
    
# if flat1 == flat2:
#     print("Да полощадь у них равна")
# else:
#     print("нет не равна")

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 > flat2)
print(flat1 >= flat2)
print(flat1 < flat2)
print(flat1 <= flat2)