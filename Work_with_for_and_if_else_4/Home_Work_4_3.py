"""
узнаём какая карта пропала
"""
#Ввод всез карт сколько есть
N  = int(input("Введите количество карт: "))

#память
CURRENT_SUM = 0

#выводим строку
print("Введите номер оставшихся катрочек: ")

#ну и начинаем запускать цикл
for _ in range(N - 1):
    CURENT_CARD = int(input())
    CURRENT_SUM += CURENT_CARD

#создаём переменую в которой будет матиматическое вычисление что бы айти сумму карт
TOTAL_SUM = N * (N + 1) // 2

#ну и находим пропавшую карту
MISSING_CARD = TOTAL_SUM - CURRENT_SUM

print("Потеряная карточка: ", MISSING_CARD)
