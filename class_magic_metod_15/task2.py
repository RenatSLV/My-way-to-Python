class Complex:
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2
    
    def __add__(self, other):
        return Complex(self.number1 + other.number, self.number2 + other.number2)
    
    def __sub__(self, other):
        return Complex(self.number1 - other.number1, self.number2 - other.number2)
    
    def __mul__(self, other):
        number1_part = self.number1 * other.number1 - self.number2 * other.number2
        number2_part = self.number1 * other.number2 + self.number2 + other.number1

        return Complex(number1_part, number2_part)
    
    def __truediv__(self, other):
        denom = other.number1 ** 2 + other.number2 ** 2
        number1_part = (self.number1 * other.number1 - self.number2 * other.number2) / denom
        number2_part = (self.number2 * other.number1 + self.number1 + other.number2) / denom

        return Complex(number1_part, number2_part)
    
    def __str__(self) -> str:
        return f"{self.number1} + {self.number2}i"

num1 = Complex(2, 5)
num2 = Complex(2, 3)

num_add = num1 - num2
print(f"Сумма: ({num1}) + ({num2}) = {num_add}")

num_sub = num1 - num2
print(f"Разность: ({num1}) - ({num2}) = {num_sub}")

num_mul = num1 * num2
print(f"Произведение: ({num1}) * ({num2}) = {num_mul}")

num_truediv = num1 / num2
print(f"Деление: ({num1}) / ({num2}) = {num_truediv}")