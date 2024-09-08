"""
нам надо просто получить время в UTC
"""
from datetime import datetime, timezone

#получаем текущие время по UTC
time_UTC = datetime.now(timezone.utc)

#Выводим время
print(f"Время в UTC: {time_UTC}")