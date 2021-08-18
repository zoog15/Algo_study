n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
num = 1

for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            a[j][m-1-i] = num
        else:
            a[n-1-j][m-1-i] = num
        num += 1

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()