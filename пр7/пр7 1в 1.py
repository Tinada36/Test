import math

def krug(r):
    s = math.pi * r * r
    return s
def treug(a,b,c):
    p = (a + b + c) / 2
    s = math.sqrt(p*(p - a) * (p - b) * (p - c))
    return s
def kv(a, b):
    s = a * b
    return s


n = input()
if n.lower() == "круг":
    r = int(input("Введите радиус"))
    print(krug(r))
elif n.lower() == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    print(treug(a,b,c))
elif n.lower() == "квадрат":
    a = int(input())
    b = int(input())
    print(kv(a,b))



