A = int(input("Введи"))
B = int(input("Введи"))
if A >= B:
    print("Неверное условие")
else:
    for i in range(A, B + 1):
        print(i, end = " ")
