import calendar

def print_calendar(year, mouth):
    cal = calendar.TextCalendar(firstweekday=0)
    
    calendar_str = cal.formatmonth(year, mouth)

    print(calendar_str)

def main():
    print("Инструкция:\nГод пешите (К примеру 2004)\nМесяц пешите (К примеру 4 == Апрель)\n")
    year = int(input("Введите год: "))
    mouth = int(input("Введите месяц: "))

    print(print_calendar(year, mouth))

if __name__ == "__main__":
    main()