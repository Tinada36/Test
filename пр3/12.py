a = int(input("введите"))
b = int(input("введите"))
if a < b:
    R = a - b + 1
elif a > b and a > 3:
    R = b * b - b
else:
    R = b * b - 1
print(R)


