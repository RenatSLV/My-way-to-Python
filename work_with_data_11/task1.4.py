from datetime import date

def addYear(d, years):
    try:
        new_date = d.replace(year=d.year + years)
    except ValueError:
        if d.month == 2 and d.day == 29:
            new_date = d.replace(year=d.year + years, month = 3, day = 1)
        else:
            raise
    return new_date

    
print(addYear(date(2015,1,1), -1))
print(addYear(date(2015,1,1), 0))
print(addYear(date(2015,1,1), 2))
print(addYear(date(2000, 2, 29), 1))