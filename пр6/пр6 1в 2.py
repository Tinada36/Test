a = []
n = int(input())
sum = 0
for i in range(0, n):
    a.append(int(input()))
    sum += a[i]
b = sum / len(a)
print(b)
