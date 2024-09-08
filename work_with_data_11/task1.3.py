from datetime import datetime,timedelta

def find_sunday(year):
    sunday = []
    first_day_of_year = datetime(year, 1, 1)

    days_to_first_sunday = (6 - first_day_of_year.weekday()) % 7
    first_sunday = first_day_of_year + timedelta(days=days_to_first_sunday)

    curent_sunday =first_sunday
    while curent_sunday.year == year:
        sunday.append(curent_sunday)
        curent_sunday += timedelta(weeks=1)

    return sunday
year = int(input("Введите год: "))

sundays = find_sunday(year)

for sunday in sundays:
    print(sunday.strftime("%d %B %Y"))