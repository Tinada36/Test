a = int(input("введите"))
b = int(input("введите"))
if a < b:
    x = 2 * a + 2 * b
elif a > b:
    x = a - b + 1
elif a == b:
    x = b * b - b
print(x)

