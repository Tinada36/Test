import math
def tr1(kat1, kat2):
    return math.sqrt(kat1 ** 2 + kat2 ** 2)
def tr2(kat1, kat2):
    return math.sqrt(kat1 ** 2 + kat2 ** 2)
if tr1(4, 5) > tr2(6, 7):
    print("Первая гипотенуза больше")
else:
    print("Вторая гипотенуза больше")