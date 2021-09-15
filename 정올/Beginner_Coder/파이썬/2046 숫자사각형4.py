import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0]*n for _ in range(n)]
num = 1

if m == 1:
    for i in range(n):
        for j in range(n):
            arr[i][j] = num
        num += 1
elif m == 2:
    for i in range(n):
        if i%2 == 0:
            num = 1
            for j in range(n):
                arr[i][j] = num
                num += 1
        else:
            num = n
            for j in range(n):
                arr[i][j] = num
                num -= 1
elif m == 3:
    for i in range(n):
        for j in range(n):
            arr[i][j] = (i+1)*(j+1)
            num += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()