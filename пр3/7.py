v = int(input("введите"))
k = int(input("введите"))
if v < 2 and k == 1:
    B = v - k + 1
elif k > v:
    B = (k * k) + (v * v)
else:
    B = k * k + v
print(B)