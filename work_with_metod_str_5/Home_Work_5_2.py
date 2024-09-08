"""
Задание №2.
"""
#это через .count
VVOD = input("Введите строку: ")

KOL_VO_PROBEL = VVOD.count(" ")
KOL_VO_SLOV = KOL_VO_PROBEL + 1

print(KOL_VO_SLOV)

#а это через len()
ss = VVOD.split()
SS = len(ss)

print(SS)
