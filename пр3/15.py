a = int(input("введите"))
b = int(input("введите"))
if a < 2 and b > 3:
    C = a + b * b
elif a > b and a > 3:
    C = b * b + 2
else:
    C = b
print (C)