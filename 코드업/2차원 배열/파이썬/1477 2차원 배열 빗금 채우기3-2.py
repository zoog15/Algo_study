n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
num = 1

for i in range(0, n+m-1):
    for j in range(0, n):
        for k in range(0, m):
            if j+k == i:
                a[j][k] = num
                num += 1

for i in range(0, n):
    for j in range(0, m):
        print(a[i][j], end=' ')
    print()
