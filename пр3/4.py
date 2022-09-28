v = int(input("введите"))
k = int(input("введите"))
if v < k:
    Z = v - k + 1
elif k < v:
    Z = (k * k) - (v * v)
else:
    Z = k * k - k
print(Z)
