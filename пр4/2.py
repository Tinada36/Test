A = int(input("Введи"))
B = int(input("Введи"))
if A < B:
    for i in range(A, B + 1):
        print(i, end=" ")
while A >= B:
    print(A, end=" ")
    A = A - 1
