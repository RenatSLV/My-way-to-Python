from datetime import datetime,timedelta

def find_first_monday(year,week_number):
    #первый день в году
    first_day_of_year = datetime(year, 1, 1)
    #первый понедельник в году
    first_monday_of_year = first_day_of_year + timedelta(days=(7 - first_day_of_year.weekday()))
    #первый понедельник даной недели
    first_monday_of_week = first_monday_of_year + timedelta(weeks=(week_number - 1))
    return first_monday_of_week

year = 2015
week_number = 50

first_monday = find_first_monday(year,week_number)

print(f"{year}, {week_number}")
print(f"пн {first_monday.strftime("%d %B %H: %M:%S %Y")}")