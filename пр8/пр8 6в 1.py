from random import randint

n = int(input("количество стоблцов "))
m = int(input("количество строк "))

a = [[randint(1 , 10) for j in range(n)] for i in range(m)]
for i in range(m):
    print(a[i],"Максимальный элемент: ", max(a[i]))
for i in range(n):
    x = [x[i] for x in a]
print("Минимальнйы элемент : ", min(x), end=" ")