n = int(input())
a = [[0]*n for _ in range(n)]
num = 1

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            a[j][i] = num
        else:
            a[n-1-j][i] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
