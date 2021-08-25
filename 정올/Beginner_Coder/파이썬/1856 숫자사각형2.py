n, m = map(int, input().split())
num = 1
a = [[0]*m for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            a[i][j] = num
            num += 1
    else:
        for j in range(m-1,-1,-1):
            a[i][j] = num
            num += 1

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()