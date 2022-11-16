f = open('Letin_Mikhail_vvod.txt')
a = [line.replace("\n", "").split() for line in f]

flag = 1
for i in range(2):
    for j in range(i + 1, 2):
        if a[i][j] != a[j][i]:
            flag = 0
if flag == 1:
    print('Всё хорошо')
else:
    print('Всё плохо')

with open('Letin_Mikhail_vivod', 'w') as f:
    if flag == 1:
        f.write('Всё хорошо')
    else:
        f.write('Всё плохо')