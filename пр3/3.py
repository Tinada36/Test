a = int(input("введите"))
b = int(input("введите"))
if a < b:
    C = a + b
elif a > b and a > 3:
    C = b * b - b
else:
    C = (b * b) - 1
print(C)
