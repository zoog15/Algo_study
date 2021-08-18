n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
num = 1

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            a[n-1-i][m-1-j] = num
        else:
            a[n-1-i][j] = num
        num += 1

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()