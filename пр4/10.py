n = int(input("Введите число"))
k = int(input("Введите число"))
fib1 = 1
fib2 = 1
sum = 2
for i in range(2, n):
    fib1 = fib2
    fib2 = fib1+fib2
    if k >= i:
        sum += fib2
print(sum)
