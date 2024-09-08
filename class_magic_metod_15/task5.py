class Roman:
    
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50, 
        'C': 100,
        'D': 500,
        'M': 1000
    }
    int_to_roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
            self.roman = self.int_to_roman(value)
        elif isinstance(value, str):
            self.roman = value
            self.value = self.roman_to_int(value)
        else:
            raise TypeError("Значение должно быть либо числа либо строка!")

    @staticmethod
    def roman_to_int(roman):
        i = 0
        num = 0
        while i < len(roman):
            if i + 1 < len(roman) and Roman.roman_to_int_map[roman[i]] < Roman.roman_to_int_map[roman[i + 1]]:
                num += Roman.roman_to_int_map[roman[i + 1]] - Roman.roman_to_int_map[roman[i]]
                i += 2
            else:
                num += Roman.roman_to_int_map[roman[i]]
                i += 1
        return num

    @staticmethod
    def int_to_roman(number):
        roman = ''
        for (num, rom) in Roman.int_to_roman_map:
            while number >= num:
                roman += rom
                number -= num
        return roman

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        else:
            raise TypeError("Операция должнабыть типа Roman")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        else:
            raise TypeError("Операция должнабыть типа Roman")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        else:
            raise TypeError("Операция должнабыть типа Roman")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        else:
            raise TypeError("Операция должнабыть типа Roman")

    def __str__(self):
        return self.roman



r1 = Roman("X")
r2 = Roman(5)
add_roman = r1 + r2
sub_roman = r1 - r2
mul_roman = r1 * r2
truediv_roman = r1 / r2

print(f"{r1} + {r2} = {add_roman}")
print(f"{r1} - {r2} = {sub_roman}")
print(f"{r1} * {r2} = {mul_roman}")
print(f"{r1} / {r2} = {truediv_roman}")