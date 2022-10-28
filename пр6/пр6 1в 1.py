a = []
n = int(input())
for i in range(0, n):
    b = int(input())
    a.append(b)
max = a[0]
for i in range(1, n):
    if a[i] > max:
        max = a[i]
print(max)
for i in range(n -1, -1, -1):
    print(a[i], end=' ')
print(max)

