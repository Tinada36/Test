a = []
n = int(input("Введите n"))

for i in range(n):
    c = input().split()
    for j in range(len(c)):
        c[j] = int(c[j])
    a.append(c)
flag = 1
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            flag = 0

if flag == 1:
    print('Хорошая работа')
else:
    print('Всё плохо')