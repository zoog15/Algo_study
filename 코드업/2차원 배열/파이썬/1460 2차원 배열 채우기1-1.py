n = int(input())

a = [[0]*n for _ in range(n)]
num = 1

for i in range(n):
    for j in range(n):
        a[i][j] = num
        num += 1

for i in a:
    for j in i:
        print(j, end=' ')
    print()