d = []
n = int(input())
for i in range(0, n):
    d.append(int(input()))
a = []
for i in range(0, n):
    if d[i] < 15:
        d[i] = d[i] * 2
for i in range(0, n):
    print(d[i], end= " ")
