A = int(input("Введи"))
B = int(input("Введи"))
while A > B:
    if A % 2 != 0:
        print(A, end=" ")
    A = A - 1
