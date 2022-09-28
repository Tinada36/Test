k = int(input("введите"))
c = int(input("введите"))
if k < 5 and c > 4:
    X = k + (c * c)
elif k > c and k > 3:
    X = (c * c) + 2
else:
    X = c - 1
print(X)

