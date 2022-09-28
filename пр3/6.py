a = int(input("введите"))
b = int(input("введите"))
if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = a * a
print(x)