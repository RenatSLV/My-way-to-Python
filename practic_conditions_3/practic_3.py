if __name__ in "__main__":
    #просим вести числа
    num = input("Введите номер свокго билета: ")
    #разделяем на 2 строки
    start = num[:3]
    end = num[3:]
    #сумируем
    start_sum = sum(int(i) for i in start)
    end_sum = sum(int(i) for i in end)
    #задаём условие
    if start_sum == end_sum:
        print("Счастливый")
    else:
        print("Обычный")
