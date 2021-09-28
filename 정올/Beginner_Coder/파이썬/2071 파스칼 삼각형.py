import sys

n, m = map(int, sys.stdin.readline().split())  # n : 삼각형의 높이, m : 파스칼 삼각형 종류

arr = [[0] * (i + 1) for i in range(n)]

for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

if m == 1:
    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()
if m == 2:
    for i in range(n):
        for k in range(i):
            print(" ",end='')
        for j in range(n-i):
            print(arr[n-i-1][j], end=' ')
        print()

if m == 3:
    for i in range(n):
        for j in range(i+1):
            print(arr[n-j-1][n-i-1], end=' ')
        print()