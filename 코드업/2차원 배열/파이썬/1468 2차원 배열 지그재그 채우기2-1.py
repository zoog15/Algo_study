n = int(input())
a = [[0]*n for _ in range(n)]
num = 1

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            a[i][j] = num
            num += 1
        else:
            a[i][n-1-j] = num
            num += 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

