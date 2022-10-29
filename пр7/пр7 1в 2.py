def summ(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum


def srzn(a):
    return summ(a) / len(a)


print('Введите первый массив')
n = input()
a = n.split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
print(summ(a), srzn(a))

print('Введите второй массив')
n = input()
a = n.split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
print(summ(a), srzn(a))

print('Введите третий массив')
n = input()
a = n.split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
print(summ(a), srzn(a))