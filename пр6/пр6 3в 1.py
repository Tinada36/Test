d = []
n = int(input())
for i in range(0, n):
    d.append(int(input()))
sum = 0
for i in range(0, n):
    if i % 2 == 1:
        sum += d[i]
for i in range(0, n):
    print(d[i], end=" ")
print()
print(sum)

