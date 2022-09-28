f = int(input("введите"))
k = int(input("введите"))
if f < k:
    R = f + k * k - 1
elif f == 3 and k < 2:
    R = k * k
else:
    R = f - 1
print(R)