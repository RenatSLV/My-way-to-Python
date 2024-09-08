from datetime import datetime
def calculate_difference(start_date,end_date):
    #Преобразуем строки в даты
    datetime
    start = datetime.strptime(start_date,"%Y-%m-%d %H:%M:%S")

    end = datetime.strptime(end_date,"%Y-%m-%d %H:%M:%S")
    #Вычесляем разницу
    deference = end - start
    #вытаскиваем дату час минуту секунду
    days = deference.days
    seconds = deference.seconds
    hours, remainder = divmod(seconds,3600)
    minuts, seconds = divmod(remainder,60)

    return days ,hours ,minuts ,seconds

#пример выполнения
start_date = '2024-06-15 12:00:00'
end_date = '2024-06-18 14:45:30'

days ,hours ,minuts ,seconds = calculate_difference(start_date, end_date)

print(f"Diference: {days} days, {hours} hours, {minuts} minuts, {seconds} seconds")
