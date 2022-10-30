a = []
n = int(input())
m = int(input())
for i in range(n):
    c = input().split()
    for j in range(len(c)):
        c[j] = int(c[j])
    a.append(c)
for i in range(n):
    for j in range(m):
        if a[i][j] > a[0][0]:
            c = a[0][0]
            a[0][0] = a[i][j]
            a[i][j] = c
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()