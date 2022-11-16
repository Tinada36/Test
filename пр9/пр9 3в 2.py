f = open('Letin_Mikhail_vvod.txt')
a = [line.replace("\n", "").split() for line in f]
n = 3
m = 3
for i in range(n):
    for j in range(m):
        if a[i][j] > a[0][0]:
            c = a[0][0]
            a[0][0] = a[i][j]
            a[i][j] = c
file = open('Letin_Mikhail_vivod.txt','w')
for i in range(n):
    file.write(' '.join(map(str, a[i])))
    file.write('\n')
file.close()