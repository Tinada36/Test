x = int(input("введите"))
y = int(input("введите"))
if x < 2 and y == 2:
    B = x * y + 1
elif x > y:
    B = y * y + x * x
else:
    B = x * x + 2
print(B)