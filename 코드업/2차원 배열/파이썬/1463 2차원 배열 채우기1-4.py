n = int(input())

a = [[0]*n for _ in range(n)]
num = 1

for i in range(n):
    for j in range(n-1, -1, -1):
        a[j][i] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
