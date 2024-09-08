def plus_two(number):
    try:
        result = number + 2
        print(result)
    except TypeError:
        print("Ожидаемый тип данных - число!")

plus_two(10)#True

plus_two(20)#True

plus_two("hello world")#False

plus_two({12:13})#False