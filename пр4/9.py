n = int(input("Введите число"))
fib1 = 1
fib2 = 1
sum = 2
for i in range(2, n + 1):
    fib1 = fib2
    fib2 = sum
    sum = fib1 + fib2
print(sum - 1)